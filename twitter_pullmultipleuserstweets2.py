#GOAL: play with location data a bit

#imports necessary methods from Twitter library
import json
import tweepy
import time
import csv
import sys

#authorises twitter
CONSUMER_KEY = 'JQTLSIh5bCwb0sWc4qPu6PmNF'
CONSUMER_SECRET = 'ump6jtorie2XqnJPvK1faEsL46A1nWykte03ZYrWHO2TQ79Sq9'
ACCESS_TOKEN = '2572709161-oJYqUylg3UFVMEDJB3MNRoih4X0D5i9zENCb8qG'
ACCESS_SECRET = 'UAtP868uKh8Gu79ChSMcMJwaHfkd1830lMbcPRzf4NebJ'

#authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#opens the .csv

#returns members of a list & some details on them 
screen_names = []
for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster", include_entities=True).items():
    screen_names.append(f"{user.screen_name}")

for i in screen_names:
    #returns all tweets of a user
    counter = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=i, tweet_mode="extended").items():
        counter = counter + 1
        print(f"{counter}\t{country}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.full_text}\t{status.favorite_count}\t{status.retweet_count}")

