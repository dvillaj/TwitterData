import tweepy
from comun.util import *

if __name__ == '__main__':

    api = tweepy.API(get_auth())

    userName = 'NoSQLDigest'

    user = api.get_user(userName)
    print ("Name: %s" % user.screen_name)
    print ("Description: %s" % user.description)
    print ("Followers count: %i" % user.followers_count)
    print ("Friends' count: %i" % user.friends_count)
    print ("Statues Count [Number of Tweets]: %i" % user.statuses_count)