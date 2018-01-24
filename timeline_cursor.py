import tweepy
import sys
from comun.util import *

if __name__ == '__main__':

    api = tweepy.API(get_auth())

    name = 'MSMK_'

    c = tweepy.Cursor(api.user_timeline,id=name).items()    
    timeline_results = []
    while True:
        try:
            tweet = c.next()
            timeline_results.append(tweet)

        except:
            print("Error: %s " % sys.exc_info()[0])
            break

    print("Timeline cursor = %i" % len(timeline_results))
    print_result(timeline_results)
    save_result_json(timeline_results, "msmk.json")