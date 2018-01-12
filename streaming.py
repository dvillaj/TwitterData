import tweepy
import json
import pprintpp

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

# Variables that contains the user credentials to access Twitter API 
consumer_key = 'dvli18J2UrO2eR26bHcxDlqW5'
consumer_secret = '4DSCvxYW0IpHPrfIAyJTUTGMznnjmWiO464WuuiTt3O7vJjqmB'
access_token = '12391902-0bZCGZcLcnYIASAGxVbzB2rOMpAcAA1wG1QfkLdzH'
access_token_secret = '6x5lXv9WbIBrsFgzzoQ8vpLr7NOQ2agy0lDlGBoTaTJua'

# This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        json = json.loads(data)
        print(data['text'])
        return True

    def on_error(self, status):
        print("Error %i" % status)


if __name__ == '__main__':
    # This handles Twitter authentication and connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)
    #stream.filter(track=['python'])
    stream.filter(track=['NoSQL'])