import tweepy
import pprintpp
from util import *

if __name__ == '__main__':

    api = tweepy.API(get_auth())

    name = 'NoSQLDigest'

    timeline_results = api.user_timeline(screen_name = name, count = 1000, include_rts = True)
    print("Timeline = %i" % len(timeline_results))
    print_result(timeline_results)

    #tweet = timeline_results[0]
    #pprintpp.pprint(tweet._json)