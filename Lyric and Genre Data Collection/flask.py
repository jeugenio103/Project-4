from flask import Flask, request, render_template
import pandas as pd
import spotipy
from tensorflow import keras
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

@app.route('/model_predict', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Get the input from the input bar
        song_name = request.form['input']
        
        # Use the Spotipy library to search for the song and retrieve the audio features
        sp = spotipy.Spotify()
        results = sp.search(q='track:' + song_name, type='track')
        audio_features = results['tracks']['items'][0]['audio_features']
        
        # Create a Pandas dataframe with the audio features
        df = pd.DataFrame([audio_features])
        
        # Preprocess the data if necessary
        df = df.dropna()
        scaler = StandardScaler()
        X_scaled = scaler.fit_transform(df)
        
        # Load the model
        model = keras.models.load_model('genre_predicting_model.h5')
        
        # Predict the genre using the model
        prediction = model.predict(X_scaled)
        
        # Return the predicted genre to the HTML template
        return render_template('index.html', input=song_name, prediction=prediction)
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run()
