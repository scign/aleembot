# Author: Aleem Juma

from threading import Thread
from flask import render_template, request, jsonify
from app import app, slack_web_client, slack_events_adapter
from app import slackops

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

def new_thread(target, **kwargs):
    kwargs['client'] = slack_web_client
    Thread(
        target=target,
        kwargs=kwargs
    ).start()

@slack_events_adapter.on('pin_added')
def newpin(payload):
    event = payload.get('event',{})
    new_thread(
        target=slackops.new_pin,
        channel=event.get('channel',''),
        item=event.get('item', {})
    )

@slack_events_adapter.on('app_mention')
def mention(payload):
    event = payload.get('event',{})
    new_thread(
        target=slackops.mention,
        channel=event.get('channel', ''),
        user=event.get('user', ''),
        text=event.get('text', '')
    )

@slack_events_adapter.on('message')
def message(payload):
    event = payload.get('event',{})
    if not event.get('user', '') in ['U01C4K43H5E','U01BCMQKNCD']:
        new_thread(
            target=slackops.message_response,
            user=event.get('user', ''),
            message=event.get('text', '')
        )

@slack_events_adapter.on('file_created')
def newfile(payload):
    event = payload.get('event',{})
    new_thread(
        target=slackops.save_file,
        file_id=event.get('file_id', '')
    )

@slack_events_adapter.on('member_joined_channel')
def newchanneljoin(payload):
    event = payload.get('event',{})
    new_thread(
        target=slackops.new_channel_member,
        channel=event.get('channel', ''),
        user=event.get('user', '')
    )

@slack_events_adapter.on('team_join')
def newteamjoin(payload):
    event = payload.get('event',{})
    new_thread(
        target=slackops.new_team_member,
        user=event.get('user', '')
    )