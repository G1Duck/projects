import twitter

#authorises twitter
CONSUMER_KEY = 'JQTLSIh5bCwb0sWc4qPu6PmNF'
CONSUMER_SECRET = 'ump6jtorie2XqnJPvK1faEsL46A1nWykte03ZYrWHO2TQ79Sq9'
OAUTH_TOKEN = '2572709161-oJYqUylg3UFVMEDJB3MNRoih4X0D5i9zENCb8qG'
OAUTH_TOKEN_SECRET = 'UAtP868uKh8Gu79ChSMcMJwaHfkd1830lMbcPRzf4NebJ'
auth = twitter.oauth.OAuth(OAUTH_TOKEN, OAUTH_TOKEN_SECRET, CONSUMER_KEY, CONSUMER_SECRET)
twitter_api = twitter.Twitter(auth=auth)

print(twitter_api)
