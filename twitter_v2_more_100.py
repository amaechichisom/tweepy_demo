import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "covid OR joe biden place_country:US"

for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=1000):
    print(tweet.id )

