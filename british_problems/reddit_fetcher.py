"""Module to handle all Reddit API related work"""

import praw

import utils


_REDDIT_USER_AGENT = 'alexa:british_problems:0.1 (by /u/alexabritishproblems)'
_REDDIT_CREDS = utils.get_credentials('reddit')

_REDDIT = praw.Reddit(user_agent=_REDDIT_USER_AGENT,
                      client_id=_REDDIT_CREDS['client_id'],
                      client_secret=_REDDIT_CREDS['client_secret'],
                      username=_REDDIT_CREDS['username'],
                      password=_REDDIT_CREDS['passwd'])

_BRITISH_PROBLEMS_SUBREDDIT = _REDDIT.subreddit('britishproblems')


def get_britishproblems_reddit(count=10):
    """Returns a list of length count (default 10, max 100)
     of submission titles from /r/britishproblems"""
    return [submission.title for submission in _BRITISH_PROBLEMS_SUBREDDIT.hot(limit=count)]
