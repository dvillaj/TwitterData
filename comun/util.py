import tweepy
from prettytable import PrettyTable
from comun.secret import consumer_key, consumer_secret, access_token, access_token_secret
import os

def get_auth():
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    return auth


def print_result(tweets, size = 20):
    table = PrettyTable(["User", "Fecha", "Texto"])
    table.align["User"] = "l"
    table.align["Texto"] = "l"

    for tweet in tweets[0:size]:
        table.add_row([tweet.user.screen_name, tweet.created_at, tweet.text[:80]])
     
    print(table)


def save_result(tweets, filepath = "results.csv"):

    if not os.path.exists("data"):
        os.makedirs("data")

    with open("data/" + filepath, 'w') as file:

        file.write("Usuario|Fecha|Texto" + os.linesep)
        
        for tweet in tweets:
            line = "%s|%s|%s" % (tweet.user.screen_name,
                tweet.created_at, 
                tweet.text.replace("\n", " "))
            
            file.write(line.encode('utf-8'))
            file.write(os.linesep)
