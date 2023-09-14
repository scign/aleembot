# Author: Aleem Juma

import os

class Config(object):
    SECRET_KEY = os.environ.get('SLACK_CLIENT_SECRET', '')
    SIGNING_SECRET = os.environ.get('SLACK_SIGNING_SECRET', '')
    VERIFICATION_TOKEN = os.environ.get('SLACK_VERIFICATION_TOKEN', '')
    TOKEN = os.environ.get('SLACK_BOT_TOKEN', '')
    CLIENT_ID = os.environ.get('SLACK_CLIENT_ID', '')
