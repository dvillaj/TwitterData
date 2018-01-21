import json
import codecs
import tweepy
import os

class MyStreamListener(tweepy.StreamListener):

    def on_data(self, data):
        try:
            decoded = json.loads(data)
            print(decoded['text'])

            if not os.path.exists("data"):
                os.makedirs("data")

            # Append to file
            with codecs.open("data/tweets_json.txt", "a", "utf-8") as myfile:
                myfile.write(data.replace('\n', '').encode('utf-8'))
                myfile.write(os.linesep)

        except Exception as e:
            print("ERROR: {}".format(e))
        finally:
            return True  # Keep listening

    def on_error(self, status): 
        print("Error %i" % status) 
