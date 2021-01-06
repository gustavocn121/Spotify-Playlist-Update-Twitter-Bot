import tweepy
from tweepy_keys import CONSUMER_API_KEY_SECRET, CONSUMER_API_KEY, ACCESS_TOKEN, ACCESS_TOKEN_SECRET
import json
import requests


def post_tweet(text):
    # Authenticate to Twitter
    auth = tweepy.OAuthHandler(CONSUMER_API_KEY, CONSUMER_API_KEY_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)

    # Create API object
    api = tweepy.API(auth, wait_on_rate_limit=True,
        wait_on_rate_limit_notify=True)

    try:
        api.verify_credentials()
        
    except:
        print("Error during authentication")

    api.update_status(text)

if __name__ == '__main__':
    post_tweet('Teste')
    print('tweeted...\n')
