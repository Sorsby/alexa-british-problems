"""Utility module providing useful functions"""
import json
import os

CREDS_FILE_PATH = "creds.json"


def get_credentials(platform):
    """Returns credentials from creds.json file for specified platform as json dict"""
    assert platform
    if os.path.exists(CREDS_FILE_PATH):
        with open(CREDS_FILE_PATH, "r") as creds_file:
            try:
                return json.load(creds_file)[platform]
            except KeyError:
                print "ERROR: Supplied platform has no credentials!"
            except IOError:
                print "ERROR: Ensure credential file is present and valid!"
