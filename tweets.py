import tweepy
from prettytable import PrettyTable
import sys
import pprintpp
import json

from secret import consumer_key, consumer_secret, access_token, access_token_secret

def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def print_result(search_results):
    table = PrettyTable(["User", "Fecha", "Texto"])
    table.align["User"] = "l"
    table.align["Texto"] = "l"

    for tweet in search_results[0:10]:
        table.add_row([tweet.user.screen_name, tweet.created_at, tweet.text[:80]])
     
    print(table)


if __name__ == '__main__':

    api = tweepy.API(get_auth())

    user = api.get_user('NoSQLDigest')
    print ("Name: %s" % user.screen_name)
    print ("Description: %s" % user.description)
    print ("Followers count: %i" % user.followers_count)
    print ("Friends' count: %i" % user.friends_count)
    print ("Statues Count [Number of Tweets]: %i" % user.statuses_count)

    lookup ='NoSQL'
    max_tweets = 200
    search_results = api.search(q=lookup, lang = 'en', count=max_tweets)
    print("NoSQL = %i" % len(search_results))
    print_result(search_results)


    timeline_results = api.user_timeline(screen_name = 'NoSQLDigest', count = 1000, include_rts = True)
    print("Timeline = %i" % len(timeline_results))
    print_result(timeline_results)

    c = tweepy.Cursor(api.user_timeline,id='NoSQLDigest').items()    
    timeline_results = []
    while True:
        try:
            tweet = c.next()
            # Insert into db
            timeline_results.append(tweet)
        except:
            print("Error: %s " % sys.exc_info()[0])
            break

    print("Timeline cursor = %i" % len(timeline_results))
    print_result(timeline_results)

    tweet = timeline_results[0]
    pprintpp.pprint(tweet._json)