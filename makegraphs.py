from pymongo import MongoClient
from flask import Flask,render_template
# import matplotlib.pyplot as plt
import json
import pandas as pd
# import matplotlib.pyplot as plt
# from matplotlib import rcParams
# from mpltools import style
# import seaborn as sns
import time
import random
from pymongo import MongoClient
# from flask_pymongo import pymongo
from flask import Flask
app = Flask(__name__)
client=MongoClient('localhost',27017)
db=client['precog']
collection=db['twitter_db']

# sns.set_palette("deep", desat=.6)
# sns.set_context(rc={"figure.figsize": (8, 4)})
# style.use('ggplot')
# rcParams['axes.labelsize'] = 9
# rcParams['xtick.labelsize'] = 9
# rcParams['ytick.labelsize'] = 9
# rcParams['legend.fontsize'] = 7
# rcParams['text.usetex'] = False
# rcParams['figure.figsize'] = 20, 10
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
	

# def plot_tweets_per_category(category, title, x_title, y_title, top_n=5):
# 	tweets_by_cat = category.value_counts()
# 	fig, ax = plt.subplots()
# 	ax.tick_params(axis='x')
# 	ax.tick_params(axis='y')
# 	ax.set_xlabel(x_title)
# 	ax.set_ylabel(y_title)
# 	ax.set_title(title)
# 	tweets_by_cat[:top_n].plot(ax=ax, kind='bar')
# 	fig.savefig("TweetLocation.png")
# 	fig.show()

# def plot_distribution(category, title, x_title, y_title):
# 	fig, ax = plt.subplots()
# 	ax.tick_params(axis='x')
# 	ax.tick_params(axis='y')
# 	ax.set_xlabel(x_title)
# 	ax.set_ylabel(y_title)
# 	ax.set_title(title)
# 	sns.distplot(category.values, rug=True, hist=True);
# 	fig.savefig("favouritecount_distribution.png")

# def plot_piechart(x_list,title):
# 	plt.pie(x_list,labels=label_list,autopct="%1.1f%%")
# 	plt.title(title)
# 	plt.savefig("original_or_retweeted.png")


@app.route('/')
def result():
	# plot_tweets_per_category(tweets['Location'], "Location of Tweets", "Location", "Number of Tweets", 200)
	# plot_distribution(tweets['favorite_count'], "Favourite count distribution", "", "")
	# plot_piechart(x_list,"Original Tweets vs Retweeted Tweets")
	return render_template('display.html',x_list=x_list)  

if __name__ == '__main__':
	app.run(debug=True)    

	