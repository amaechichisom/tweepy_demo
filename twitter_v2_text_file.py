import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "covid OR joe biden"

file_name = 'tweets.txt'

with open(file_name, 'a+') as filehandler:
    for tweet in tweepy.Paginator(client.search_recent_tweets, query=query, max_results=100).flatten(limit=200):
        filehandler.write('%s\n' % tweet.id)

