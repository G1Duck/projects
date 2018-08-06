#GOAL: pull all tweets from all users who are memberis of a list.

#imports necessary methods from Twitter library
import json 
import tweepy
import time
import csv
import sys
from collections import Counter
from prettytable import PrettyTable
import itertools
import collections
from datetime import date
import calendar
from urllib.parse import urlparse
import numpy as np
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

#pulls the users from the list, and writes details to a file! 
for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster", include_entities=True).items():
    screen_names.append(f"{user.screen_name}")
    s.writerow([user.screen_name, user.location, user.statuses_count, user.followers_count, user.description, user.friends_count, user.name])
    print(f"{user.screen_name}\t{user.location}\t{user.statuses_count}\t{user.followers_count}\t{user.description}\t{user.friends_count}\t{user.name}") #this would print out a list of usernames & locations
for i in screen_names:
    #returns all tweets of a user
    counter = 0
    for status in tweepy.Cursor(api.user_timeline, screen_name=i, since="2017-07-04", tweet_mode="extended").items():
        #opening up lists which are per row 
        tags = []
        urls = []
        locations = []
        users = []
        #managing the time stamps
        time = status.created_at
        time_year = time.year
        time_month = time.month
        time_hour = time.hour
        tweet = status.full_text
        time_DoW = calendar.day_name[time.weekday()]
        time_conc_DoW_hour = str(time_DoW) + "_" + str(time_hour)
        #loops to iterate through status entities 
        for word in tweet.split():
            word_list.append(word)
        for hashtag in status.entities['hashtags']:
            tags.append(hashtag['text'])
            hashtags_list.append(hashtag['text'])
        for url in status.entities['urls']:
            urls.append(url['expanded_url'])        
            url_P_1 = (urlparse(url['expanded_url']))
            urls_domain.append(url_P_1.netloc)
        for user in status.entities['user_mentions']:
            users.append(user['screen_name'])
            user_mentions.append(user['screen_name'])
        #adding time variables to time related lists
        hour_list.append(time_hour)
        DoW_list.append(time_DoW)
        hour_and_DoW_list.append(time_conc_DoW_hour)
        year_list.append(time_year)  
        #a counter whilst testing
        counter = counter + 1 
        #if counter > 2:
        #     break 
        print(f"{counter}\t{status.user.location}\t{tags}\t{urls}\t{users}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{time_year}\t{time_month}\t{time_hour}\t{time_DoW}\t{time_conc_DoW_hour}\t{status.full_text}\t{status.favorite_count}\t{status.retweet_count}")


print("SUCCESSFUL!")
#put full lists to the side to print
#print(f"{urls_domain}")
