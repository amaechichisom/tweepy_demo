import tweepy
import pandas as pd
import config

api_key =  config.api_key
api_key_secret = config.api_key_secret

access_token = config.access_token
access_token_secret = config.access_token_secret




class Listener(tweepy.StreamingClient):

    tweets = []
    # limit = 1

    # def on_status(self, status):
    #     self.tweets.append(status)
    #     # print(status.user.screen_name + ": " + status.text)

    #     if len(self.tweets) == self.limit:
    #         self.disconnect()
    
    def on_tweet(self, tweet):
        print(stream_tweet.running)
        print(tweet)
        print(self.tweets)
        print(tweet.created_at)
        self.tweets.append([tweet['id'], tweet['text']])
        
    # def on_response(self, response):
    #     print(response)
    #     return super().on_response(response)
    
    # def on_includes(self, includes):
    #     print(includes)
    #     return super().on_includes(includes)
        
    # def on_data(self, raw_data):
    #     msg = json.loads(raw_data)
    #     if('bitcoin' in msg['data']['text']):
    #        print(msg['data'])
    #     return super().on_data(raw_data)

    def on_connection_error(self):
        self.disconnect()



stream_tweet = Listener(str(config.bearer_token))

print(stream_tweet.on_connect())
print(config.bearer_token)

# deleting rule
rule_ids = []
result = stream_tweet.get_rules()
if(result.data != None):
    for rule in result.data:
        print(f"rule marked to delete: {rule.id} - {rule.value}")
        rule_ids.append(rule.id)
    
    if(len(rule_ids) > 0):
        stream_tweet.delete_rules(rule_ids)
        stream_tweet = Listener(str(config.bearer_token))
    else:
        print("no rules to delete")
        
        
    
stream_tweet.add_rules(tweepy.StreamRule("bitcoin OR cardano"))
stream_tweet.filter(expansions=['attachments.poll_ids', 'referenced_tweets.id'], tweet_fields=["attachments", "author_id", "created_at", "entities", "geo", 'id', "lang", 'public_metrics', 'source', 'text'], user_fields=['created_at', 'description', 'entities', 'location', 'name', 'username'])
# stream_tweet.filter()

# stream_tweet.sample()
