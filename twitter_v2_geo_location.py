import tweepy
import config

client = tweepy.Client(bearer_token=config.bearer_token)

query = "covid OR joe biden place_country:US"

response = client.search_recent_tweets(query=query, max_results=100, tweet_fields=['created_at', 'lang'], user_fields=['profile_image_url'] ,expansions=['geo.place_id'])

places = {v['id']: v for v in response.includes['places']}


# for tweet in response.data:
#     if places[tweet.geo['place_id']]:
#         place = places(tweet.geo['places_id'])
#         print(tweet.id)
#         print(place.full_name)
    
    
