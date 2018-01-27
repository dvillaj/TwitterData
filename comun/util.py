import tweepy
from prettytable import PrettyTable
from comun.secret import consumer_key, consumer_secret, access_token, access_token_secret
import os
import json

def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth

def mkdir(dir_name):
    if not os.path.exists(dir_name):
        os.makedirs(dir_name)

def print_result(tweets, size = 20):
    table = PrettyTable(["User", "Fecha", "Texto"])
    table.align["User"] = "l"
    table.align["Texto"] = "l"

    for tweet in tweets[0:size]:
        table.add_row([tweet.user.screen_name, tweet.created_at, tweet.text[:80]])
     
    print(table)


def save_result(tweets, filepath = "results.csv"):

    mkdir("data")
    with open("data/" + filepath, 'w') as file:

        file.write("Usuario|Fecha|Texto" + os.linesep)
        
        for tweet in tweets:
            line = "%s|%s|%s" % (tweet.user.screen_name,
                tweet.created_at, 
                tweet.text.replace("\n", " "))
            
            file.write(line.encode('utf-8'))
            file.write(os.linesep)


def save_result_json(tweets, filepath = "results.json"):

    mkdir("data")
    with open("data/" + filepath, 'w') as file:
        for tweet in tweets:
            file.write(json.dumps(tweet._json))
            file.write(os.linesep)

def save_json(str_json, filepath = "results.json"):

    mkdir("data")
    with open("data/" + filepath, 'a') as file:
        json.dump(str_json, file)
        file.write(os.linesep)
