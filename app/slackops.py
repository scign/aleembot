# Author: Aleem Juma

def message_response(client, user, message, channel='D01BDH7USJH'):
    client.chat_postMessage(
        channel=channel,
        text=f'*{user}* mentioned me, saying: {message}'
    )

def save_file(client, file_ref):
    file_url = client.files_info(file=file_ref).get('file',{}).get('url_private_download','')

def new_channel_member(client, channel, user):
    pass

def new_team_member(client, user):
    pass

def new_pin(client, channel, item):
    pass

def mention(client, user, message):
    pass