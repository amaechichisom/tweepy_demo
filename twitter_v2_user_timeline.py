import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

# users = client.get_users_tweets(usernames=['twitterdev'])

# for user in users:
#     print(user)


tweets = client.get_users_tweets(id=2244994945, tweet_fields=['lang'])

for tweet in tweets.data:
    # print(tweet)
    print(tweet.id)
    print(tweet.lang)
