#GOAL: to analyse the results of tweets pulled
#SOME ANALYSIS STUFF IN HERE

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
import twitter_auth

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#opens the csv 
#f = csv.writer(open('user_tweets.csv', 'w'))
#f.writerow(["No.","User ID", "Username", "Tweet Time", "Tweet"])

counter = 0
#prints off to the console
print("UPDATE ME!")
word_list = [] #this has to go above the line because otherwise we get a mii list of words PER tweet
screen_names_full = []
word_list_minus = ["I", "at", "the", "a", "like", "and", "have", "to", "them", "then", "they", "she", "her", "him", "his", "it", "in", "of", "to", "these", "those", "for", "my", "he", "I've", "I'm"]

for status in tweepy.Cursor(api.user_timeline, screen_name="daniellameaneyy", tweet_mode="extended").items():
    tags = []
    urls = []
    tweet_list = []
    tweet = status.full_text
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
    for user in status.entities['user_mentions']:
            screen_names.append(user['screen_name'])
            screen_names_full.append(user['screen_name'])

    tweet_list.append(status.full_text)
    #screen_names_full.append(status.entities.screen_name) 
    #print("attempt one")
    #print(f"{screen_names_full}\n**********")
    #print("end of attempt one")
    counter = counter + 1
    #if counter > 550:    #commented out break
    #    break 
#print(f"{screen_names_full}") NOTE: if you want to print the full result, intend @ wall
word_list_clean = list(set(word_list) - set(word_list_minus))
print(word_list_clean)



#calculate word counts 
counter = collections.Counter(word_list_clean)
#print(counter.most_common())
#calculate screen names most mentioned
#counter2 = collections.Counter(screen_names_full)
#print(counter.mostcommon())

#make a pretty table for it
for label, data in (('Word', word_list_clean),
                    ('Original Word', word_list),
                    ('Screen_name', screen_names_full)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:20]]
    pt.align[label], pt.align['Count'] = 'l', 'r' 
    print(pt)

