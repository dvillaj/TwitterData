import tweepy
import codecs
import json
from secret import consumer_key, consumer_secret, access_token, access_token_secret


def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


class MyStreamListener(tweepy.StreamListener):

    def on_status(self, status):
        # When a tweet is published it arrives here.
        print(status.text.encode("ascii", errors='replace'))  # Console output may not be UTF-8
        print("-"*10)

            # Append to file
        with codecs.open("tweets.txt", "a", "utf-8") as myfile:
            myfile.write(status.text)

    def on_data(self, data):
        try:
            decoded = json.loads(data)
            print(decoded['text'])
        except Exception as e:
            print("ERROR: {}".format(e))
        finally:
            return True  # Keep listening

if __name__ == '__main__':
    print("===== My Application =====")

    # Get an API item using tweepy
    auth = get_auth()  # Retrieve an auth object using the function 'get_auth' above
    api = tweepy.API(auth)  # Build an API object.

    # Connect to the stream
    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    #print(">> Listening to tweets about #python:")
    #myStream.filter(track=['python'])

    # LOCATIONS. Use http://boundingbox.klokantech.com/ for boundingboxes
    SPAIN_GEOBOX = [-9.38,36.05,3.35,43.75]
    myStream.filter(languages=["es"], locations=SPAIN_GEOBOX)

    # End
    print("c'est fini!")