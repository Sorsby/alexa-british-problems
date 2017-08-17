"""Module to handle Alexa functionality via intents as defined in AWS Skill Builder"""
import random
import reddit_fetcher as rf

from flask import Flask
from flask_ask import Ask, question, session, statement

APP = Flask(__name__)
ASK = Ask(APP, "/")


@ASK.launch
def start_skill():
    """Entry point for opening the Alexa Skill"""
    welcome_message = 'Hello there, would you like to hear a very British problem?'
    return question(welcome_message)


@ASK.intent("YesIntent")
@ASK.intent("GetNewBritishProblem")
def handle_get_problem_intent():
    """Gets a new problem for reading out to the user"""
    british_problem = random.choice(rf.get_britishproblems_reddit())
    response_msg = "Here's one I found... " + british_problem
    return statement(response_msg)


@ASK.intent("NoIntent")
def handle_no_intent():
    """Quits the skill with a goodbye message"""
    goodbye_message = 'Are you sure? Ok... bye then!'
    return statement(goodbye_message)
