import json
import os

import twitter

CREDS_FILE_PATH = "creds.json"
TWITTER_SCREEN_NAME = "SoVeryBritish"

if os.path.exists(CREDS_FILE_PATH):
    with open(CREDS_FILE_PATH, "r") as CREDS_FILE:
        try:
            TWITTER_CREDS = json.load(CREDS_FILE)['twitter']
        except IOError:
            print "ERROR: Ensure credential file is present and valid!"


API = twitter.Api(consumer_key=TWITTER_CREDS['consumer_key'],
                  consumer_secret=TWITTER_CREDS['consumer_secret'],
                  access_token_key=TWITTER_CREDS['access_token_key'],
                  access_token_secret=TWITTER_CREDS['access_token_secret'])


def get_soverybritish_tweets():
    """Gets tweets from @SoVeryBritish"""
    try:
        tweets = API.GetUserTimeline(screen_name=TWITTER_SCREEN_NAME)
        return tweets
    except twitter.error.TwitterError as e:
        print "Couldn't fetch tweets because: " + e.message[0]['message']
