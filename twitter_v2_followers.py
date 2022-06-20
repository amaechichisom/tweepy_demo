import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)


# users = client.get_users_followers(id=2244994945, user_fields=['profile_image_url'] )

# for user in users.data:
#     print(user.name)
#     print(user.profile_image_url)
    
    
users = client.get_users_following(id=2244994945, user_fields=['profile_image_url'] )

for user in users.data:
    print(user.name)
