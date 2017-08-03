from pymongo import MongoClient
from flask import Flask,render_template
import json
import pandas as pd
import time
import random
from pymongo import MongoClient
# from flask_pymongo import pymongo
from flask import Flask
app = Flask(__name__)
client=MongoClient('localhost',27017)
db=client['precog']
collection=db['twitter_db']


tweets_data = []
for data in collection.find().batch_size(400000):
	tweets_data.append(data)

tweets = pd.DataFrame()
tweets['user'] = map(lambda tweet: tweet['user']['screen_name'], tweets_data)
tweets['text'] = map(lambda tweet: tweet['text'].encode('utf-8'), tweets_data)
tweets['Location'] = map(lambda tweet: tweet['place']['country'] if tweet['place'] != None else None, tweets_data)
tweets['retweet_count'] = map(lambda tweet: tweet['retweet_count'], tweets_data)
tweets['favorite_count'] = map(lambda tweet: tweet['favorite_count'], tweets_data)


list_of_original_tweets = [element for element in tweets['text'].values if not element.startswith('RT')]
num_originaltweets=str(len(list_of_original_tweets))
list_of_retweets = [element for element in tweets['text'].values if element.startswith('RT')]
num_retweets=str(len(list_of_retweets))
x_list=[num_originaltweets,num_retweets]
label_list=["Original Tweets","Retweeted Tweets"]
#print tweets['favorite_count']




@app.route('/')
def originalvsretweets():
	# plot_tweets_per_category(tweets['Location'], "Location of Tweets", "Location", "Number of Tweets", 200)
	# plot_distribution(tweets['favorite_count'], "Favourite count distribution", "", "")
	# plot_piechart(x_list,"Original Tweets vs Retweeted Tweets")
	return render_template('display.html',x_list=x_list)  

@app.route('/locationwise')
def location():
	counts = tweets['Location'].to_dict()
	new_count=dict()
	for key,value in counts.items():
		if value != None:
			new_count[key]=value
	#print json.dumps(new_count)
	return render_template('geoplotting.html',category=json.dumps(new_count))


@app.route('/favouritecount')
def favourite():
	#plot_distribution(tweets['favorite_count'], "Favourite count distribution", "Number of likes", "Number of tweets")
	return render_template('favourite_count.html',fav=json.dumps(tweets['favorite_count'].to_dict()))

if __name__ == '__main__':
	app.run(debug=True)    

	