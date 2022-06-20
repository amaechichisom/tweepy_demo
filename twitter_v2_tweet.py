import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)
    
    
users = client.get_liking_users(id=1538667505916461056)

for user in users.data:
    print(user.username)


# users = client.get_retweeters(id=1538667505916461056)

# users = client.get_tweet(id=1538667505916461056, tweet_fields=["created_at"])