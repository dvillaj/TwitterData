import tweepy

from comun.util import *
from comun.listeners import *

if __name__ == '__main__':
    print("===== My Application =====")

    auth = get_auth()  
    api = tweepy.API(auth) 

    myStreamListener = MyStreamListener()
    myStream = tweepy.Stream(auth=api.auth, listener=myStreamListener)

    #print(">> Listening to tweets about #python:")
    #myStream.filter(track=['python', 'NoSQL'])

    # LOCATIONS. Use http://boundingbox.klokantech.com/ for boundingboxes
    SPAIN_GEOBOX = [-9.38,36.05,3.35,43.75]
    myStream.filter(languages=["es"], locations=SPAIN_GEOBOX)

    print("c'est fini!")