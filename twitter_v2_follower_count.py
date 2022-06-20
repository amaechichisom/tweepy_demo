import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "python"

file_name = 'tweets.txt'

counts = client.get_recent_tweets_count(query=query, granularity='day')

for count in counts.data:
    print(count)

