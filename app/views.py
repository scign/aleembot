# Author: Aleem Juma

from flask import render_template, request, jsonify
from app import app, slack_web_client, slack_events_adapter
from app import slackops
from threading import Thread

@app.route('/') 
def home(): 
    return '<h1>Working!</h1>'

"""
event['type'] = Event name e.g. reaction_added, etc.
event['event_ts'] = Timestamp of the message (e.g. 1469470591.759709). event_ts, team_id, (user_id | channel_id) is intended to be unique.
event['user'] = User who initiated the event (e.g. U061F7AUR)
event['ts'] = Timestamp of the event (may be before event_ts)
event['item'] = Data specific to the underlying object type being described
"""

@slack_events_adapter.on('app.mention')
def mention(payload):
    event = payload.get('event', {})
    user_id = event.get('user', {}).get('id')
    message = event.get('item', '')
    slack_web_client.chat_postMessage(
        channel='D01BDH7USJH',
        text=f'{user_id} mentioned me: ' + message
    )

@slack_events_adapter.on('file.created')
def newfile(payload):
    pass

@slack_events_adapter.on('member.joined.channel')
def newchanneljoin(payload):
    pass

@slack_events_adapter.on('pin.added')
def newpin(payload):
    pass

@slack_events_adapter.on('reaction.added')
def newreaction(payload):
    pass

@slack_events_adapter.on('team.join')
def newteamjoin(payload):
    pass
