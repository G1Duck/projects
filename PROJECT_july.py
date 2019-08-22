#GOAL: pull all tweets from all users who are memberis of a list.
#deals with timeouts on twitter

#imports necessary methods from Twitter library
import json
import tweepy
import time as systime
import csv
import sys
from collections import Counter
from prettytable import PrettyTable
import itertools
import collections
import calendar
from urllib.parse import urlparse
import numpy as np
import twitter_auth

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#opens screen name .csv
#s = csv.writer(open('labour_user_detail.csv', 'w'))
#s.writerow(["Screen_name", "User_location", "Statuses_count", "Followers_count", "User_description", "Friends_count", "Name"])

#opens the tweet list .csv
#f = csv.writer(open('labour_csv_tweets.csv', 'w'))
#f.writerow(["counter", "user.location", "tags", "urls", "users", "user.id", "screen_name", "status.created_at", "time_year", "time_month", "time_hour", "time_DoW", "time_conc_DoW_hour",  "status.full_text", "status.favorite_count", "status.retweet_count"])

#making lists for analysis at a later point
screen_names = []
word_list = []
screen_names_full = []
hour_list = []
DoW_list = []
urls_big_list = []
urls_domain = []
hashtags_list = []
user_mentions = []
hour_and_DoW_list = []
year_list = []

#counters dictionaries - calculating from the above lists
word_counter = collections.Counter(word_list)
urls_counter = collections.Counter(urls_domain)
user_mentions_counter = collections.Counter(user_mentions)
hashtags_counter = collections.Counter(hashtags_list)
hour_and_DoW_counter = collections.Counter(hour_and_DoW_list)
years_counter = collections.Counter(year_list)

#!*!*!*! BEGINNINGS OF CSVS CREATION!*!*!*!

#with open('word_count.csv', 'w') as dm:
#    td = csv.writer(dm)
#    td.writerows(word_counter.items())

#pulls the users from the list, and writes details to a file!
try:
    for user in tweepy.Cursor(api.list_members, slug="uk-mps-labour", owner_screen_name="tweetminster", include_entities=True).items():
        screen_names.append(f"{user.screen_name}")
        print(f"{user.screen_name}\t{user.location}\t{user.statuses_count}\t{user.followers_count}\t{user.description}\t{user.friends_count}\t{user.name}") #this would print out a list of usernames & locations
        for i in screen_names:
            #returns all tweets of a user
            counter = 0
            try:
                for status in tweepy.Cursor(api.user_timeline, screen_name=i, tweet_mode="extended").items():
                    backoff_counter = 1
                    #opening up lists which are per row
                    #managing the time stamps
#                    time = status.created_at
                    users = []
                    tags = []
                    urls = []
#                    time_year = time.year
#                    time_month = time.month
#                    time_hour = time.hour
                    tweet = status.full_text
#                    time_DoW = calendar.day_name[time.weekday()]
#                    time_conc_DoW_hour = str(time_DoW) + "_" + str(time_hour)
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
#                    hour_list.append(time_hour)
#                    DoW_list.append(time_DoW)
#                    hour_and_DoW_list.append(time_conc_DoW_hour)
#                    year_list.append(time_year)
                    #a counter whilst testing
                    counter = counter + 1
                    print(f"{counter}\t{tags}\t{urls}\t{users}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.id}\t{status.full_text}")
            except tweepy.TweepError:
                systime.sleep(60 * 5)
                auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
                auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
                api = tweepy.API(auth, wait_on_rate_limit=True)
                print("tweep error avoided: tweepy.TweepError XXX1")
                continue

except tweepy.TweepError:
    systime.sleep(60 * 5)
    auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
    auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
    api = tweepy.API(auth, wait_on_rate_limit=True)
    print("tweep error avoided: tweepy.TweepError XXX2")


print("SUCCESSFULLY RUN")
