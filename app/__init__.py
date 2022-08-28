# Author: Aleem Juma

from flask import Flask
from slack import WebClient
from slackeventsapi import SlackEventAdapter
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

slack_events_adapter = SlackEventAdapter(
    signing_secret=app.config['SIGNING_SECRET'],
    endpoint='/slack/events',
    server=app
)

slack_web_client = WebClient(
    token=app.config['TOKEN']
)

from app import views