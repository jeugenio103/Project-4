# Project #4
> Project 4 will go through music features that Spotify API provides to visualize the differences within different genres. Incorporate machine learning to train our model to filter through lyrics and identify what genre the lyrics/song is from. Create a lyric generator by putting a word/ genre in and having the generator produce lyrics through the training model.<br><br>
	
ETL:<br>
Query specific genre playlists from spotify<br>
Curate genre, lyrics, meta-data from artists into DF<br>
Load data to a aws/google database to query for ML<br>
<br><br>
ML Features:<br> 
Allow users to input keywords and select a genre to develop their own 88Rising song lyrics using our saved machine learning model<br><br>

Data Retrieval:<br>
Scrape Genius lyrics 88rising songs we have listed from project 3.<br>
Spotify API - Draw music features to visualize and to also possibly create music based on a designated genre.<br>
<br><br>

Group Members:  Jeremiah Eugenio, Emilio Guzman, Kristy Le, Samantha Seng, Evelyn Votran
<br>
<br>

## Table of Contents
* [General Info](#general-information)
* [Features](#features)
* [Music Analysis](#Music-Analysis)
* [Conclusion](#Conclusion)
* [Resources](#Resources)
* [Acknowledgements](#acknowledgements)
<!-- * [License](#license) -->


## General Information



## Features
List the ready features here:
- Genre Predictor
- Lyric Generator

## Genre Predictor
We created a Genre Predictor using a Machine Learning Model, Spotify API, and by web scraping the Genius Lyrics website. We created the initial dataframe from the audio features taken by Spotify API and list of genres from web scraping the Genius website. Then we scaled the data and used a SVC Model in order to predict what genre a song would be based on its audio features. The 5 genres we chose to focus on were Pop, R&B, Rock, Country, and Rap. We were able to get about 60% accuracy.

The way the Genre Predictor works is that we input a song in the search bar, it pulls data from the Spotify API to obtain the audio features, then the audio features are used to predict the genre of the song using the model.

Because this is based on audio features, it does have difficulty predicting songs that wouldn’t normally fit in the 5 main genres such as EDM or more Indie Music and also it would have difficulty with songs that have audio feature levels not normally associated with their specific genre. Also, since genres are a bit subjective it would also affect our model. Overall, we could improve our accuracy by utilizing a larger dataset 


## Music Analysis
Gather Spotify Music Features that go into select genres:<br>
Acousticness, Duration_ms, Instrumentalness, Key, Loudness, Mode
Speechiness, Tempo, Time_signature, Valence, Popularity, featured, danceability, energy, key, loudness, mode, Speechiness, liveness

## Conclusions





## Resources
http://organizeyourmusic.playlistmachinery.com/<br>
https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3<br>
https://www.activestate.com/blog/how-to-build-a-lyrics-generator-with-python-recurrent-neural-networks/<br>
https://www.twilio.com/blog/generating-lyrics-in-the-style-of-your-favorite-artist-with-python-openai-s-gpt-3-and-twilio-sms<br>
https://marianaossilva.github.io/DSW2019/index.html<br>
https://github.com/johnwmillr/LyricsGenius<br>
https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/<br><br>
