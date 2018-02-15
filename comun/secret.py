# -*- coding: utf-8 -*-

import os
import sys

def consumer_key(): return get_enviroment_var('TWITTER_CONSUMER_KEY')
def consumer_secret(): return get_enviroment_var('TWITTER_CONSUMER_SECRET')
def access_token(): return get_enviroment_var('TWITTER_ACCESS_TOKEN')
def access_token_secret(): return get_enviroment_var('TWITTER_ACCESS_TOKEN_SECRET')

def get_enviroment_var(var):
    if os.environ[var] is None:
        print("Error. No está definida la variable de entorno %s" % var)
        sys.exit(1)

    return os.environ[var]