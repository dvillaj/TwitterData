import tweepy
from comun.util import *

if __name__ == '__main__':

    api = tweepy.API(get_auth())

    lookup ='NoSQL'

    max_tweets = 200
    search_results = api.search(q=lookup, lang = 'en', count=max_tweets)
    print("NoSQL = %i" % len(search_results))
    print_result(search_results)

    save_result(search_results, "lookup.csv")
