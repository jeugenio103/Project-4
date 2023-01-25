#Import dependecies 
from flask import Flask, request, render_template
from sqlalchemy import create_engine
# import sqlalchemy
import pandas as pd

from config import client_id, client_secret, password

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

# from pathlib import Path
from spotipy.oauth2 import SpotifyClientCredentials
import spotipy

# import sys

#Tokenize Spotify Authorization
client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

#Connect to intial AWS PostgreSQL Databaseengine 
engine = create_engine(f'postgresql://postgres:{password}@final-project-db.coodiqlcstgq.us-east-1.rds.amazonaws.com:5432/final_project_db')
# print(final_df.dtypes)

#Loading CSV File 
url = 'https://amazonsampledata.s3.amazonaws.com/equalized_data.csv'
df = pd.read_csv(url)
df = df.drop(columns=['Unnamed: 0','index','track','artist'])

#Standerdize/fit meta-data 
scaler = StandardScaler()
scaled_data = scaler.fit_transform(df[["acousticness","energy","liveness","loudness","speechiness","valence","tempo","time_signature","danceability","key","instrumentalness","mode"]])

#Select Target variables 
X = df.drop("primary_genre", axis=1)
y = df["primary_genre"].values

#Encode y target and set train/test variable split 
label_encoder = LabelEncoder()
y = label_encoder.fit_transform(y)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.33, stratify=y, random_state=42)

scaler = StandardScaler().fit(X_train)
X_train_scaled = scaler.transform(X_train)
X_test_scaled = scaler.transform(X_test)

#Set up deployment app route 
application = Flask(__name__,template_folder='templates',static_url_path='/static')

@application.route('/')
def home():
    return render_template('index.html')

@application.route('/visualization')
def visualization():
    return render_template('visualization.html')

@application.route('/lyrics_analysis')
def lyrics_analysis():
    return render_template('lyrics_analysis.html')

@application.route('/lyric_gen')
def lyric_gen():
    return render_template('lyric_gen.html')

@application.route('/about')
def about():
    return render_template('about.html')

@application.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        track_name = request.form.get('input')
        
        #Set input variable api call to initialize dataframe 
        if track_name:
            df2 = None
            results = sp.search(q=track_name, type="track", limit=1)
            track = results["tracks"]["items"][0]
            artist_name = track['artists'][0]['name']
            features = sp.audio_features(track["id"])[0]

            #Create prediction dataframe
            df2 = pd.DataFrame([features])
            df2 = df2.loc[:,["key","mode","time_signature","acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","valence","tempo"]]
            
            #Create dataframe to append to database table 
            final_df = pd.DataFrame(columns=["artist","track","genre","key","mode","time_signature","acousticness","danceability","energy","instrumentalness","liveness","loudness","speechiness","valence","tempo"])
            
            #Load model 
            pickled_model = pickle.load(open('svm_model.pkl', 'rb'))
            df2_scaled = scaler.transform(df2)

            prediction = pickled_model.predict(df2_scaled)
            predicted_genre = label_encoder.inverse_transform(prediction)
            prediction_string = "".join(predicted_genre)
            prediction_string = prediction_string.replace('[','').replace(']','')
            
            #Append genre and meta-data to final_df then export to AWS instance 
            try:
                if prediction_string:
                    final_df.at[0, 'genre'] = prediction_string
                    final_df.at[0,'artist'] = artist_name
                    final_df.at[0,'track'] = track_name

                for col in df2.columns:
                    final_df.at[0, col] = df2.at[0,col]

                final_df[["key","mode","time_signature","acousticness","danceability","energy","instrumentalness","liveness",\
                        "loudness","speechiness","valence","tempo"]] = final_df[["key","mode","time_signature","acousticness","danceability",\
                        "energy","instrumentalness","liveness","loudness","speechiness","valence","tempo"]]\
                        .apply(pd.to_numeric, errors='coerce')
                
                final_df['genre'] = final_df['genre'].astype('str')
                final_df['artist'] = final_df['artist'].astype('str')
                final_df['track'] = final_df['track'].astype('str')

                #Check for correct format
                print(final_df)
                print(final_df.dtypes)

                #Append to final table scheme 
                final_df.to_sql("final_df", engine, if_exists='append', index=False)

            except Exception as e:
                print('An error occurred: ', e)

        else:
            prediction_string = " "
        
        # Return the predicted genre to the HTML template
    return render_template('index.html', input=track_name, prediction_string=prediction_string)


@application.route('/lyric', methods=['GET','POST'])
def lyric():
    topic = request.form["topic"]
    artist = request.form["artist1"]
    from openai_key import key 
    
    prompt_text = "Artist: {} \n\nTopic: {} \n\nLyrics:\n".format(artist, topic)

    import openai
    openai.api_key = key
    response = openai.Completion.create(
    model="davinci:ft-personal-2023-01-05-06-24-18",
    prompt=prompt_text,
    max_tokens=256,
    temperature=0.7,
    frequency_penalty=0.5,
    stop=["\n###END"]
)

    lyric_string = "".join(response['choices'][0]['text'])

    
    def format_lyrics(lyrics):
        from string import ascii_letters, punctuation
        nl_char_after = "])"
        nl_char_before = "["
        
        allowed = set(ascii_letters)
        allowed_punc = set(punctuation)
        allowed |= allowed_punc
        allowed |= set(" ")
        
        lyric_str = ""
        prev_char = ""
        for char in lyrics:
            if char in allowed:
                if char in nl_char_after:
                    lyric_str = lyric_str + char + "\n"
                elif char in nl_char_before or ((prev_char not in allowed) and char.isupper()):
                    lyric_str = lyric_str + "\n" + char
                else:
                    lyric_str = lyric_str + char
                prev_char = char
            else:
                prev_char = char

        new_str = ""
        for index in range(0, len(lyric_str)):
            if lyric_str[index] == '#':
                break
            if index+1 == len(lyric_str):
                new_str = new_str + lyric_str[index]
                break
            else:
                prev = lyric_str[index]
                after = lyric_str[index+1]
                if prev in allowed_punc or prev == " ":
                    new_str = new_str + prev
                elif prev.islower() and after.isupper():
                    new_str = new_str + prev + "\n"
                else:
                    new_str = new_str + prev
        # Remove any double spaces
        import re
        new_str = re.sub(' +', ' ', new_str)
        return new_str
    import string
    lyric_array = format_lyrics(lyric_string)
    lyric_array = lyric_array.split('\n')
    return render_template('lyric_gen.html', topic=topic, lyric_string=lyric_array, artist=artist)




if __name__ == '__main__':
    application.run(debug=True)