# Author: Aleem Juma

from flask import render_template, request, jsonify
from app import app, slack_events_adapter
from threading import Thread

@app.route('/') 
def home(): 
    return '<h1>Working!</h1>'

@slack_events_adapter.on('message')
def message(payload):
    event = payload.get('event', {})
    print(event)