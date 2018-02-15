import tweepy
from comun.util import *
import sys

if __name__ == '__main__':

    try:

        api = tweepy.API(get_auth())
        api.get_user('dvillaj')
        print("All good!")

    except tweepy.error.TweepError as e:
        if isinstance(e.message, list) and ('message' in e.message[0]):
            error = e.message[0]['message']
        else:
            error = e.message

        print("Connection error: %s" % error)