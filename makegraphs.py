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
print tweets['favorite_count']

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

# count=0
# di={"10-20":0, "20-30":0,"30-40":0,"40-50":0,"50-60":0, "60-70":0, "70-80":0, "80-90":0, "90-100":0, ">=100":0}
# for ele in tweets['favorite_count']:
# 	if ele is None:
# 		count+=1
# 	elif ele >=0 and ele<10:
# 		key=di.get('0-10')
# 		key+=1
# 		di['0-10']=key
# 	elif ele >=10 and ele<20:
# 		key=di.get('10-20')
# 		key+=1
# 		di['10-20']=key
# 	elif ele >=20 and ele<30:
# 		key=di.get('20-30')
# 		key+=1
# 		di['20-30']=key
# 	elif ele >=30 and ele<40:
# 		key=di.get('30-40')
# 		key+=1
# 		di['30-40']=key
# 	elif ele >=40 and ele<50:
# 		key=di.get('40-50')
# 		key+=1
# 		di['40-50']=key
# 	elif ele >=50 and ele<60:
# 		key=di.get('50-60')
# 		key+=1
# 		di['50-60']=key
# 	elif ele >=60 and ele<70:
# 		key=di.get('60-70')
# 		key+=1
# 		di['60-70']=key
# 	elif ele >=70 and ele<80:
# 		key=di.get('70-80')
# 		key+=1
# 		di['70-80']=key
# 	elif ele >=80 and ele<90:
# 		key=di.get('80-90')
# 		key+=1
# 		di['80-90']=key
# 	elif ele >=90 and ele<100:
# 		key=di.get('90-100')
# 		key+=1
# 		di['90-100']=key
# 	else:
# 		key=di.get('>=100')
# 		key+=1
# 		di['>=100']=key


# print di

@app.route('/')
def originalvsretweets():
	# plot_tweets_per_category(tweets['Location'], "Location of Tweets", "Location", "Number of Tweets", 200)
	# plot_distribution(tweets['favorite_count'], "Favourite count distribution", "", "")
	# plot_piechart(x_list,"Original Tweets vs Retweeted Tweets")
	return render_template('display.html',x_list=x_list)  

@app.route('/locationwise')
def location():
	return render_template('geoplotting.html',category=tweets['Location'])


@app.route('/favouritecount')
def favourite():
	#plot_distribution(tweets['favorite_count'], "Favourite count distribution", "Number of likes", "Number of tweets")
	return render_template('favourite_count.html',fav=tweets['favorite_count'])

if __name__ == '__main__':
	app.run(debug=True)    

	