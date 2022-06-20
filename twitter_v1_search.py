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
# user = 'AmaechiLegend'
# limit=300

# tweets = tweepy.Cursor(api.user_timeline, screen_name=user, count=200, tweet_mode='extended').items(limit)

# search tweets
# keywords = ['Bitcoin', 'Ethereum', 'XRP', 'Tether', 'Cardano', 'Polkadot', 'Stellar', 'USDT', 'Dogecoin', 'Chainlink']
# limit=20

keyword = "South Africa"

structure = tweepy.Cursor(api.search_tweets, q=keyword, count=10, tweet_mode='extended').items(10)

for tweet in structure:
    print(tweet.user.screen_name)


# Tweets = api.user_timeline(screen_name=user, count=limit, tweet_mode='extended')



# create DataFrame
columns = ['postid', 'date', 'title', "url", "article", "source", "read_time", "category", "author", "views", "user description"]
columns = ['postid', 'date']
data = []

for tweets in keywords:
    tweetlist = tweepy.Cursor(api.search_tweets, q=tweets, count=10, tweet_mode='extended').items(limit)
    for tweet in tweetlist:
        data.append([tweet.id_str, tweet.created_at, tweets, tweet.user.url, tweet.full_text, "Twitter", "none", tweets, tweet.user.screen_name, tweet.user.followers_count, tweet.user.description])

df = pd.DataFrame(data, columns=columns)

print(df)

df.to_csv('Twitter-data.csv')
