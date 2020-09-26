# Author: Aleem Juma

from flask import render_template, request, Response
from app import app
from threading import Thread

@app.route('/') 
def home(): 
    return '<h1>Working!</h1>'

@app.route('/slack/events')
def handle_event():
    try:
        data = request.json
        if data['token'] != app.config('VERIFICATION_TOKEN'):
            return Response(status=403)
        if data.get('type','') == 'url_verification':
            return {"challenge": data['challenge']}
    return Response(status=500)
