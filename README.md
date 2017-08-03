#PrecogTask

Task A

Web development framework used: Flask
Tweepy RESTful API used to stream data from twitter.


FILES AND DIRECTORIES

- requirements.txt 
 Includes all the libraries used in the application.

- hashtags.txt
 This file contains the advanced search queries for various hashtags mentioning Narendra Modi or/and Arvind Kejriwal. Presently I am using 7 hashtags to filter out the tweets.

- database_insert.py
 This script collects slightly above 10000 tweets with relevant hashtags from twitter and stores it into a collection called "twitter_db" in the database "precog" in mongodb.
 Ideally, one would need multiple API keys to access this many tweets as the API rate limit is 180 tweets per 15 minutes window per user authentication, but the workaround used here requires only 1 set of API keys. 
 The above is well explained in this blog: https://dev.to/bhaskar_vk/how-to-use-twitters-search-rest-api-most-effectively

- makegraphs.py
 This script accesses tweets from the database and stores them in alltweets. 
 Then we can use the tweets to run further analysis on them and pass the result via the result function to the display.html template in order to display it.
 This script also runs the flask server.

Interactive and dynamic graphs have been made using highcharts. 

- templates
Contains the html files.

- Static
 Contains the javascript file. 


SETUP

1. pip freeze requirements.txt - this installs all the required libraries, if not present on your system.
2. Open a terminal and type mongod to get the server running. In a new terminal, type mongo.
3. use precog database and create a collection called twitter_db
4. python database_insert.py - collects relevant tweets from twitter and puts into the database. 
5. Check count of the tweets in the database. Should be at least 10000.
6. python makegraphs.py - runs the flask server and displays the content.
7. Open 127.0.0.1:5000, that is the flask server, to view the graphs.