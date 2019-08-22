#GOAL: pulls details from a list of users!

import json
import sys
#imports necessary methods from Twitter library
import tweepy
import time
import csv
import configparser
import os
import getpass
import twitter_auth

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

f = csv.writer(open('labour_followers_python.csv', 'w'))
f.writerow(["Screen_name", "User_name", "User_description", "User_location", "User_follower_count", "User_friends_count", "User_verified_flag"])

#from a list of users, report their twitter info
print("Screen name\tName\tUser Description\tUser status count\tLocation\tFollower count\tFriends count\tVerified flag")
for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster").items():
    print(f"{user.screen_name}\t{user.name}\t{user.description}\t{user.statuses_count}\t{user.location}\t{user.followers_count}\t{user.friends_count}\t{user.verified}")
    #writes a row to the .csv - needs to be in array output!!!
    f.writerow([user.screen_name,user.name,user.description,user.statuses_count,user.location,user.followers_count,user.friends_count,user.verified])
