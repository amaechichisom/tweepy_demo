import tweepy
import configparser
import pandas as pd
import config

config = configparser.ConfigParser()
config.read('config.ini')

auth = tweepy.OAuth1UserHandler(
    config['twitter']['api_key'], config['twitter']['api_key_secret'], config['twitter']['access_token'], config['twitter']['access_token_secret']
)

try:
    api = tweepy.API(auth)
    print("successfully connected")
    
except:
    print("connection unsuccessful")
    

# user tweets
user = 'veritasium'
limit=300

tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# create DataFrame
columns = ['User', 'Tweet']
data = []

for tweet in tweets:
    data.append([tweet.user.screen_name, tweet.full_text])

df = pd.DataFrame(data, columns=columns)

print(df)

