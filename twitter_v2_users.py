import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "covid "

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'] ,expansions=['author_id'])

users = {v['id']: v for v in response.includes['users']}

print(users)

for tweet in response.data:
    if users[tweet.author_id]:
        # print(tweet)
        user = users[tweet.author_id]
        print(user.username)
        print(user.profile_image_url)
