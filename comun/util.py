import tweepy
from prettytable import PrettyTable
from comun.secret import consumer_key, consumer_secret, access_token, access_token_secret

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

    with open("data/" + filepath, 'w') as file:

        file.write("Usuario\tFecha\tTexto\n")
        
        for tweet in tweets:
            line = "%s\t%s\t%s\n" % (tweet.user.screen_name,
                weet.created_at, 
                tweet.text)
            
            file.write(line)
