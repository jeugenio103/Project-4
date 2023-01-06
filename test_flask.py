from flask import Flask, request, render_template
import pandas as pd

from config import client_id, client_secret

from tensorflow import keras 
import tensorflow as tf

from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.preprocessing import OneHotEncoder
from sklearn.model_selection import train_test_split

from pathlib import Path
import sklearn as skl
import spotipy
import numpy as np
from spotipy.oauth2 import SpotifyClientCredentials


client_credentials_manager = SpotifyClientCredentials(client_id,client_secret)
sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

file_path = Path("./Test-Data/final_genre_12k.csv")
df1 = pd.read_csv(file_path)

X = df1.drop("primary_genre", axis=1)
y = df1["primary_genre"].values

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=85)


app = Flask(__name__)
@app.route('/')
def test():
    return render_template('test.html')


@app.route('/predict', methods=['GET','POST'])
def predict():
    if request.method == 'POST':
        # Get the track name from the form data
        track_name = request.form.get('input')

        if track_name:
            # Search for the track
            results = sp.search(q=track_name, type="track", limit=1)

            # Get the first track from the search results
            track = results["tracks"]["items"][0]
            # Get the track's audio features
            features = sp.audio_features(track["id"])[0]
            # Create a Pandas DataFrame with one row
            df2 = pd.DataFrame([features])

            # Preprocess the data
            model_X = df2.drop(columns={'type','id','uri','track_href','analysis_url'})
            X_scaler = StandardScaler()
            X_scaled = X_scaler.fit_transform(model_X)
            X_scaled = X_scaled.reshape(-1, 13)

            model = keras.models.load_model('test_model.h5')
            prediction = model.predict(X_scaled)

            prediction_index = np.argmax(prediction, axis=1)
            y_original = y_train

            prediction_decoded = [y_original[prediction_index[i]] for i in range(prediction_index.shape[0])]

            prediction_string = "".join(prediction_decoded)
            prediction_string = prediction_string.replace('[','').replace(']','')
        else:
            prediction_string = ""

        
        # Return the predicted genre to the HTML template
        return render_template('test.html', input=track_name, prediction_string=prediction_string)


    else:
        return render_template('test.html')


if __name__ == '__main__':
    app.run(debug=True)
