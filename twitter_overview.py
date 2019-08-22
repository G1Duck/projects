##!/usr/bin/python3.6 #establishes which version of python this'll run in
#uses a query

import json
import sys
#imports necessary methods from Twitter library
import tweepy
import configparser
import os
import getpass
import twitter_auth

#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

counter = 0


print("count\ttweet ID\ttweet content\tuser screen name\tURLs\thashtags") #print a title row
for tweet in tweepy.Cursor(api.search,
                           q="#loveisland",
                           count=100,
                           result_type="recent",
                           include_entities=True,
                           lang="en").items():
    #start declaring variables here!
    tags = []
    favorite_count = tweet.favorite_count
    retweeted = tweet.retweeted
    text = tweet.text
    tweet_id = tweet.id
    source = tweet.source
    in_reply_to_screenname = tweet.in_reply_to_screen_name
    retweet_count = tweet.retweet_count
    user_screename = tweet.user.screen_name
    user_location = tweet.user.location
    user_bio = tweet.user.description
    user_followers_count = tweet.user.followers_count
    user_friends_count = tweet.user.friends_count
    urls = []
    users_mentioned = []
    created_at = tweet.created_at

    for hashtag in tweet.entities['hashtags']:
        tags.append(hashtag['text'])
    for url in tweet.entities['urls']:
        urls.append(url['expanded_url'])
    for user_mention in tweet.entities['user_mentions']:
        users_mentioned.append(user_mention['screen_name'])


    print(f"{counter}\t{tweet_id}\t{text}\t{retweet_count}\t{user_screename}\t{urls}\t{tags}\t{users_mentioned}")
    counter = counter + 1
    if counter > 100:
        break
