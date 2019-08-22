#GOAL: to further analyse tweets

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
import matplotlib.pyplot as plt

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#opens the csv
#f = csv.writer(open('user_tweets.csv', 'w'))
#f.writerow(["No.","User ID", "Username", "Tweet Time", "Tweet"])

counter = 0
#prints off to the console

word_list = [] #this has to go above the line because otherwise we get a mii list of words PER tweet
screen_names_full = []
hour_list = []
DoW_list = []
urls_big_list = []
urls_domain = []


for status in tweepy.Cursor(api.user_timeline, screen_name="daniellameaneyy", tweet_mode="extended").items():
    tags = []
    urls = []
    tweet_list = []
    tweet = status.full_text
    #managing the time stamps
    time = status.created_at
    time_year = time.year
    time_month = time.month
    time_hour = time.hour
    time_DoW = calendar.day_name[time.weekday()]
    #concatenates the two
    time_conc_DoW_hour = str(time_DoW) + "_" + str(time_hour)
    screen_names = []
    #splits a tweet into its words, adds it to the mega word list
    for word in tweet.split():
        word_list.append(word)
    #print(word_list)
    for user in screen_names:
        screen_names_full.append(user)
    for hashtag in status.entities['hashtags']:
            tags.append(hashtag['text'])
    for url in status.entities['urls']:
            urls.append(url['expanded_url'])
            url_P_1 = (urlparse(url['expanded_url']))
            urls_domain.append(url_P_1.netloc)
    for user in status.entities['user_mentions']:
            screen_names.append(user['screen_name'])
            screen_names_full.append(user['screen_name'])
    #defining time variables
    hour_list.append(time_hour)
    tweet_list.append(status.full_text)
    DoW_list.append(time_DoW)
    #defining URL vars
    print(f"{tweet}")
#print(f"{urls_domain}")

    #prints time  summary
    #print(f"{time_conc_DoW_hour}\t{time}\t{calendar.day_name[time.weekday()]}\t{time.hour}\t{time.month}\t{time.year}")
    #a counter to cap the number of tweets used
    #counter = counter + 1
    #if counter > 550:    #commented out break
    #    break

#print(f"{urls_big_list}")
#print(f"{screen_names_full}") NOTE: if you want to print the full result, intend @ wall

#calculate word counts - THIS PRINTS THE FULL LIST!
#counter = collections.Counter(word_list)
#print("word list and count")
#print(f"{word_list}\t{counter}")
#print(counter)
#calculate screen names most mentioned
#counter2 = collections.Counter(screen_names_full)
#print(counter.mostcommon())


#counter for hour list
#hour_counter = Counter(hour_list)
#print(f"Hour counter:\t{hour_counter}")

#make a pretty table for it
#for label, data in (('Original Word', word_list),
 #                   ('Screen_name', screen_names_full),
 #                   ('Hour of day', hour_list),
 #                   ('Day of Week', DoW_list),
 #                   ('URLs', urls_domain)):
 #   pt = PrettyTable(field_names=[label, 'Count'])
 #   c = Counter(data)
 #   [pt.add_row(kv) for kv in c.most_common()[:20]]
 #   pt.align[label], pt.align['Count'] = 'l', 'r'
#    print(pt)

#import itertools
#create bar chart
#print(hour_counter)

#graph_hours = list(hour_counter.keys())
#graph_values = list(hour_counter.values())

#plt.bar(range(len(hour_counter)),graph_values,tick_label=graph_hours)
#plt.savefig('bar.png')
#plt.show()

#URLS COUNTER HERE
urls_counter = collections.Counter(urls_domain)
print(urls_counter)

#!*!*! PUT IN AN EXPORTER TO .CSV! !*!*!*!
with open('julycsv.csv', 'w') as dm:
    td = csv.writer(dm)
    td.writerows(urls_counter.items())



#version two of the URL csv (using stack overflow) !!!*!*!*!*!*! PAY ATTENTION
#u2 = csv.writer(open('URLsDANIELLA.csv', 'w'))
#u2.writerow([urls_counter.items()])

