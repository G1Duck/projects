#GOAL: pull all tweets from all users who are memberis of a list.

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

#opens the .csv
f = csv.writer(open('labour_csv_tweets.csv', 'w'))
f.writerow(["No", "User Location", "Hashtags", "URLs", "User_ID", "Screen_name", "Tweet_created_at", "Full_tweet", "Favourite_count", "Retweet_count"])

#returns members of a list & some details on them 
screen_names = []
for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster", include_entities=True).items():
    screen_names.append(f"{user.screen_name}")
#   print(f"{user.screen_name}\t{user.location}") #this would print out a list of usernames & locations
for i in screen_names:
    #returns all tweets of a user
    counter = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=i, tweet_mode="extended").items():
        tags = []
        urls = []
        locations = []
        for hashtag in status.entities['hashtags']:
            tags.append(hashtag['text'])
        for url in status.entities['urls']:
            urls.append(url['expanded_url'])        

        counter = counter + 1 
        print(f"{counter}\t{status.user.location}\t{tags}\t{urls}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.full_text}\t{status.favorite_count}\t{status.retweet_count}")
        f.writerow([counter, status.user.location, tags, urls, status.user.id, status.user.screen_name, status.created_at, status.full_text, status.favorite_count, status.retweet_count])

