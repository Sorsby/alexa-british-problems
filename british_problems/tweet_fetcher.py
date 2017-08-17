"""Module to handle all twitter API related work"""

import twitter

import utils

_TWITTER_SCREEN_NAME = "SoVeryBritish"
_TWITTER_CREDS = utils.get_credentials('twitter')

API = twitter.Api(consumer_key=_TWITTER_CREDS['consumer_key'],
                  consumer_secret=_TWITTER_CREDS['consumer_secret'],
                  access_token_key=_TWITTER_CREDS['access_token_key'],
                  access_token_secret=_TWITTER_CREDS['access_token_secret'])


def get_soverybritish_tweets():
    """Gets tweets from @SoVeryBritish"""
    try:
        tweets = API.GetUserTimeline(
            screen_name=_TWITTER_SCREEN_NAME, count=200)
        return tweets
    except twitter.error.TwitterError as ex:
        print "Couldn't fetch tweets because: " + ex.message[0]['message']
