#GOAL: play with location data a bit

#imports necessary methods from Twitter library
import json
import tweepy
import time
import csv
import sys
import twitter_auth

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
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
