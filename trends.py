import tweepy
from pprint import pprint as pp

from comun.util import *


if __name__ == "__main__":

    api = tweepy.API(get_auth())
    json = api.trends_place(23424950) # Yahoo WOEID

    save_json(json, filepath = "trends.json")

    pp(json)