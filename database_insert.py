import tweepy
import json
import sys
import os
from pymongo import MongoClient

consumer_key="wB6NRjsWw2pzi8gKoh2elv0yR"
consumer_secret="MCrjytSgnVWCG5ClNRv8KHes68KCAfXBfq1iIVNi5fOdhI9i7p"
access_token="809769609658146816-GzgGBagA5k6moiLvj9VpFcztoGxuItD"
access_token_secret="BGLKs1ljy2dTuIV6npRstt2U8u7FoY1wVmEXzQN77WKUz"

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)

client=MongoClient('localhost',27017)
db=client['precog']
collection=db['twitter_db']

queries=[]
with open('hashtags.txt') as f:
    for line in f:
        line = line.strip('\n')
        queries.append(line)

MAX_TWEETS=10000
max_id = -1L
sinceId = None
tweetCount = 0
tweetsPerQry=100
searchQuery=queries[0] or queries[1] or queries[2] or queries[3] or queries[4] or queries[5] or queries[6]
while tweetCount<MAX_TWEETS:
	try:
		if max_id<=0:
			if not sinceId:
				new_tweets=api.search(q=searchQuery, count=tweetsPerQry)
			else:
				new_tweets=api.search(q=searchQuery, count=tweetsPerQry, sinceId=sinceId)
		else:
			if not sinceId:
				new_tweets=api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id-1))
			else:
				new_tweets=api.search(q=searchQuery, count=tweetsPerQry, max_id=str(max_id-1), sinceId=sinceId)
		if not new_tweets:
			print "No new tweets found"
			break
		for tweet in new_tweets:
			tweet_data=tweet._json
			collection.insert(tweet_data)
		tweetCount += len(new_tweets)
		max_id = new_tweets[-1].id
	except tweepy.TweetError as e:
		print "some error: " + str(e)
		break

			