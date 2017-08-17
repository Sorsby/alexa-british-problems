"""Module to handle all Reddit API related work"""
import json
import time

import requests
import unidecode


def get_british_problems_reddit():
    """Get the titles of the /r/britishproblems posts"""
    user_pass_dict = {'user': 'alexabritishproblems',
                      'passwd': '83O9ls8eC77lmO%3@rw&',
                      'api_type': 'json'}
    sess = requests.Session()
    sess.headers.update(
        {'User-Agent': 'alexa:british_problems:0.1 ' +
         '(by /u/alexabritishproblems)'})

    sess.post('https://wwww.reddit.com/api/login', data=user_pass_dict)
    time.sleep(1)
    url = "https://www.reddit.com/r/britishproblems/top/.json?limit=50"
    html = sess.get(url)
    data = json.loads(html.content.decode('utf-8'))

    titles = [unidecode.unidecode(listing['data']['title'])
              for listing in data['data']['children']]
    return titles
