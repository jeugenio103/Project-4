# Project #4
> Project 4 will go through music features that Spotify API provides to visualize the differences within different genres. Incorporate machine learning to train our model to filter through audio features and identify what genre the song is from. Create a lyric generator by putting a word/ genre in and having the generator produce lyrics through the training model.<br><br>
	
ETL:<br>
Query specific genre playlists from spotify<br>
Curate genre, lyrics, meta-data from artists into DF<br>
Load data to a aws/google database to query for ML<br>

ML Features:<br> 
Allow users to input keywords and select a genre to develop their own 88Rising song lyrics using our saved machine learning model

Data Retrieval:<br>
Scrape Genius lyrics 88rising songs we have listed from project 3.<br>
Spotify API - Draw music features to visualize and to also possibly create music based on a designated genre.<br>

Group Members:  Jeremiah Eugenio, Emilio Guzman, Kristy Le, Samantha Seng, Evelyn Votran
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

## Music Features
As shown, we successfully scraped over 10,000 mainstream song features, but we noticed a skewed distribution when analyzing the genre count within our mainstream artist dataset. Pop was a high outlier, with 5,000 songs compared to the maximum count of other genres. 

When comparing this to our 88 Rising data, we observed that Pop and Rap were the leading genres amongst 88rising artist.

The main features with higher prominent values  were danceability, energy, mode, and valence. These were highly indicative in equalizing our data set, as well as  transforming our training values by dropping unnecessary features like duration. As this made a factor in our genre classification.

Music tempo values ranged between 117 and 125, thus, there was no clear correlation between mainstream and 88Rising music data when testing our model.

On average, mainstream music had lower compressed and adjusted loudness compared to 88Rising genre style music. However, under Spotify interface, spotify does standardize loudness to not exceed -1 or -2 dB to avoid distortion and transcoding issues for track feature analysis. 

Our last images are word clouds with the most frequent word usage per genre. Most of the words can be categorized as filler words, but we can see how certain words are dominant for specific genres, such as love and profanity for Pop and Rap.

## Lyric Generator
We decided to create a model that generates 88rising lyrics using GPT-3 from OpenAi. We built and tuned the model using the davinci engine to fit the language of our 88Rising artist data.  
 
Let’s say we wanted to generate a song for Rich Brian with the topic of Hype Time.
Our model takes in the artist name and the topic of the song to generate the lyrics. 
Here are the results! 

If I want the hype, I'll get the hype (Uh)<br>
If I want the money, well, then I'ma get the money (Uh)<br>
If I want a bad bitch then I'ma get a bad bitch (Uh)<br>
          
I don't need your opinion 'cause this ain't about you (About you)<br>
I was born in ' , but I'm living in ' now (Now)<br>
You don't know me, bitch just follow what they own'Cause it's no time for your scumbag attitude<br>
I'm so focused on where I'm going that my eyes are closed'Cause I don't need to see the road when I've rode it so many times(So many times)<br>
          <br>
When you ready for me then let me know (Let me know)<br>
When you ready to drop then let me show (Show)<br>
When you ready for this shit then let's go (Let's go)<br>

## Lyric Analysis
Now that we have our generated lyrics, it looks great to the human eye, but how accurate are these lyrics with the 88Rising artist language? Thus, we decided to generate two lyrics, and look into the similarities between the generated vocabulary and our artists’ actual vocabulary. The two artists we used are Rich Brian and Joji. For Joji, we selected the topic of Young Energy, and this is the lyrics generated. As you can see, it’s not bad for a Joji song. It definitely matches Joji’s low valence attribute (so sad boy vibes). For Rich Brian, we used the topic of Hype Time. Taking a look at the lyrics, it has rap music components such as spot stacks that help with the flow such as “uh” that matches Rich Brian’s language.   
 
Down here, we explored the vocabulary of each artist. Here we have the word bank for Joji. As you can see the top word joji uses are … 
 
Below, we checked the similarity of words between each line of our generated lyric and the word bank. In Joji’s first line, we have a word similarity ratio of 50% excluding stop words. Therefore, 50% of the words used in this line are in Joji’s lyric vocabulary.  
 
Here we have the word bank for Rich Brian. His top word is “ayy” which is used as a spot stack. Down here, we have the similarity ratios for each line.  
 
From there, we created an artist predictor module using natural language processing and naïve bayes model to classify the artist. Nevertheless, our model produced an accuracy of 46% which is not good. When testing our model on these two generated lyrics, it predicted Rich Brian Hype Time with an accuracy of 70.59% and a score of 16.67% for Joji Young Energy.

I would improve our artist prediction model by incorporating other features such as finding the average number of words per line and data on bars, stanzas, and sentence semantics.

## Conclusions
As we reflect upon our project, we can understand why current big companies still decide to have genres and tags categorized through human touch. As recommendation algorithms have been at the forefront of retaining and gaining new users in many entertainment and social media industries, understanding the nuances of a genre or tag has become imperative in their success. Professional genre tagger, Greg Harty, of Netflix explained that

 “Giving a movie the category of cerebral romantic psychodrama is a bit more involved than simply saying it’s a thriller.” 

Artists.spotify.com explained,

“We define genres based on info from listener playlists (title, description, etc.) and our music curation teams. We don’t use info from metadata or the playlist pitching tool in Spotify for Artists.

We recognize genres constantly evolve and songs can cross different genres. The way we assign songs to genres may change over time, and we may add new genres too.”

Though our model’s accuracy score can be improved by inputting more data and fine tuning with more resources, the most effective way to pick up the ever evolving nuanced genres and tags is with human touch, at this time. 





## Resources
http://organizeyourmusic.playlistmachinery.com/<br>
https://medium.com/swlh/how-to-leverage-spotify-api-genius-lyrics-for-data-science-tasks-in-python-c36cdfb55cf3<br>
https://www.activestate.com/blog/how-to-build-a-lyrics-generator-with-python-recurrent-neural-networks/<br>
https://www.twilio.com/blog/generating-lyrics-in-the-style-of-your-favorite-artist-with-python-openai-s-gpt-3-and-twilio-sms<br>
https://marianaossilva.github.io/DSW2019/index.html<br>
https://github.com/johnwmillr/LyricsGenius<br>
https://www.analyticsvidhya.com/blog/2020/10/feature-selection-techniques-in-machine-learning/<br><br>
