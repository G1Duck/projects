
#imports necessary methods from Twitter library
import json 
import tweepy
import time
import csv
import sys
import configparser
import os
import getpass

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

#opens the csv 
f = csv.writer(open('/var/www/daniella.work/daniellatweets.csv', 'w'))
f.writerow(["number","user_id", "Username", "twet_time", "tweet", "fav_count", "RT_flag"])

counter = 0
#prints off to the console
#print("Counter\tUser ID\tUsername\tTweet time\tTweet\tFavourite_count\tRT_count")
for status in tweepy.Cursor(api.user_timeline, screen_name="daniellameaneyy", tweet_mode="extended").items():
    counter = counter + 1
#    print(f"{counter}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.full_text}\t{status.favorite_count}\t{status.retweeted}")
    f.writerow([counter, status.user.id, status.user.screen_name, status.created_at, status.full_text, status.favorite_count, status.retweeted])

#    if counter > 49:
#        break


