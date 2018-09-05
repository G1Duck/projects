#GOAL: pull all tweets from all users who are memberis of a list.
#deals with timeouts on twitter

#imports necessary methods from Twitter library
import json 
import tweepy
import csv
import sys
from collections import Counter
import itertools
import collections
import calendar
import configparser
import os
import time as systime 
import twitter_auth 

config = configparser.RawConfigParser()
config_file = os.path.expanduser('~/.twitter.conf')
config.read(config_file)

CONSUMER_KEY = config.get('twitter', 'CONSUMER_KEY')
CONSUMER_SECRET = config.get('twitter', 'CONSUMER_SECRET')
ACCESS_TOKEN = config.get('twitter', 'ACCESS_TOKEN')
ACCESS_SECRET = config.get('twitter', 'ACCESS_SECRET')

#authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#opens screen name .csv
#s = csv.writer(open('labour_user_detail.csv', 'w'))
#s.writerow(["Screen_name", "User_location", "Statuses_count", "Followers_count", "User_description", "Friends_count", "Name"])

#opens the tweet list .csv
f = csv.writer(open('/var/www/daniella.work/labour_csv_tweets.csv', 'w'))
f.writerow(["counter", "screen_name", "user_followers_count", "full_tweet", "status_created_at", "fav_count", "RT_count", "userID"])

#making lists for analysis at a later point
screen_names = []

for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster", include_entities=True).items():
    if user.screen_name not in screen_names:
        screen_names.append(f"{user.screen_name}")

for i in screen_names:
    counter = 0
    try: 
        for status in tweepy.Cursor(api.user_timeline, screen_name=i, tweet_mode="extended").items():
            if 'RT' in status.full_text:
                continue
            counter = counter + 1 
            print(f"{counter}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.id}\t{status.full_text}")
            f.writerow([counter, user.screen_name, user.followers_count, status.full_text, status.created_at, status.favorite_count, status.retweet_count, user.id])
            if counter > 4:
                break
    except tweepy.TweepError:
        systime.sleep(60 * 5)
        auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
        auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
        api = tweepy.API(auth, wait_on_rate_limit=True)
        print("tweep error avoided: tweepy.TweepError XXX1")
        continue



