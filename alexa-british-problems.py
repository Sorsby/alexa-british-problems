import json
import time
import random

import requests
import unidecode
from flask import Flask
from flask_ask import Ask, question, session, statement

APP = Flask(__name__)
ASK = Ask(APP, "/")


def get_british_problems():
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


@ASK.launch
def start_skill():
    """Entry point for the alexa skill"""
    welcome_message = 'Hello there, would you like to hear a very British problem?'
    return question(welcome_message)


@ASK.intent("YesIntent")
@ASK.intent("GetNewBritishProblem")
def handle_get_problem_intent():
    """Handles the intent for getting a new british problem and outputting it to Alexa"""
    british_problem = random.choice(get_british_problems())
    response_msg = "Here's one I found... " + british_problem
    return statement(response_msg)


@ASK.intent("NoIntent")
def handle_no_intent():
    """Handles an intent to exit the skill and not receive a problem"""
    goodbye_message = 'Are you sure? Ok... bye then!'
    return statement(goodbye_message)
