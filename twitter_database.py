#GOAL: save tweets to a database

#imports necessary methods from Twitter library
import json 
import tweepy
import time
import csv
import sys
import mysql.connector
import twitter_auth

cnx = mysql.connector.connect(user='daniella', password='XXXXXX',
				unix_socket='/var/run/mysqld/mysqld.sock',
				database='daniellastweets',
                                charset = 'utf8mb4')

cursor = cnx.cursor()

#authorises twitter
#authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

counter = 0
#prints off to the console
print("Counter\tUser ID\tUsername\tTweet time\tTweet")
for status in tweepy.Cursor(api.user_timeline, screen_name="daniellameaneyy", tweet_mode="extended").items():
    counter = counter + 1
    print(f"{counter}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.full_text}")

    add_to_database = ("INSERT INTO tweets "
                       "(counter, userID, screen_name, status_created_at, tweet) "
                       "VALUES (%s, %s, %s, %s, %s)")


#creating an array with all tweet info
    tweet_array = ( counter, status.user.id, status.user.screen_name, status.created_at, status.full_text )

    cursor.execute(add_to_database, tweet_array)
    cnx.commit()

#closes at end of loop
cursor.close()
cnx.close()


