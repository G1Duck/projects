#GOAL: save tweets to a database

#imports necessary methods from Twitter library
import json 
import tweepy
import time
import csv
import sys
import mysql.connector

cnx = mysql.connector.connect(user='daniella', password='munck1n',
				unix_socket='/var/run/mysqld/mysqld.sock',
				database='daniellastweets',
                                charset = 'utf8mb4')

cursor = cnx.cursor()

#authorises twitter
CONSUMER_KEY = 'JQTLSIh5bCwb0sWc4qPu6PmNF'
CONSUMER_SECRET = 'ump6jtorie2XqnJPvK1faEsL46A1nWykte03ZYrWHO2TQ79Sq9'
ACCESS_TOKEN = '2572709161-oJYqUylg3UFVMEDJB3MNRoih4X0D5i9zENCb8qG'
ACCESS_SECRET = 'UAtP868uKh8Gu79ChSMcMJwaHfkd1830lMbcPRzf4NebJ'

#authorisations
auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_SECRET)
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


