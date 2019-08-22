#GOAL: return the sentiment for a number of tweets

#imports everything
import sys
import csv
import tweepy
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from collections import Counter
from aylienapiclient import textapi
import twitter_auth
if sys.version_info[0] < 3:
    input = raw_input

#aylien credentials
application_id = "969ed6bf"
application_key = "2627811d7c0000135c5ba6823b24c965"

#further twitter authorisations
auth = tweepy.OAuthHandler(twitter_auth.CONSUMER_KEY, twitter_auth.CONSUMER_SECRET)
auth.set_access_token(twitter_auth.ACCESS_TOKEN, twitter_auth.ACCESS_SECRET)
api = tweepy.API(auth, wait_on_rate_limit=True)

#sets up an instance of the AYLIEN text API
client = textapi.Client(application_id, application_key)

#opens the csv
f = csv.writer(open('user_tweets.csv', 'w'))
f.writerow(["No.", "Sentiment", "Sentiment Subjectivity", "User ID", "Username", "Tweet Time", "Tweet"])

#defines some variables to be used
tweet_list = []
sentiment_list = []

counter = 0
#prints off to the console
print("Counter\tSentiment\tSentiment Subjectivity\tUser ID\tUsername\tTweet time\tTweet")
for status in tweepy.Cursor(api.user_timeline, screen_name="daniellameaneyy", tweet_mode="extended").items():
    dirty_tweet = status.full_text
    tidy_tweet = dirty_tweet.strip().encode('ascii', 'ignore')
    tweet_list.append(f"{tidy_tweet}")
    counter = counter + 1

    #send to get a response
    response = client.Sentiment({'text': tidy_tweet})
    sentiment_print = response['polarity']
    subjectivity_marker = response['subjectivity']
    #append to a counter for sentiment
    sentiment_list.append(sentiment_print)
    #print out and add to .csv too
    print(f"{counter}\t{sentiment_print}\t{subjectivity_marker}\t{status.user.id}\t{status.user.screen_name}\t{status.created_at}\t{status.full_text}")
    f.writerow([counter, sentiment_print, subjectivity_marker, status.user.id, status.user.screen_name, status.created_at, status.full_text])
    if counter > 49:
        break

print(sentiment_list)

#sentiment counter
sent_counter = Counter(sentiment_list)
print(sent_counter.most_common())
print("*" * 30)

for label, data in (('Sentiment', sentiment_list),
                    ('Sentiment', sentiment_list)):
    pt = PrettyTable(field_names=[label, 'Count'])
    c = Counter(data)
    [pt.add_row(kv) for kv in c.most_common()[:20]]
    pt.align[label], pt.align['Count'] = 'l', 'r'
    print(pt)
