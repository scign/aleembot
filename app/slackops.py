# Author: Aleem Juma

def message_response(client, user, message):
    client.chat_postMessage(
        channel='D01BDH7USJH',
        text=f'*{user}* mentioned me, saying:/n/n{message}'
    )

def save_file(client, file_ref):
    file_url = client.files_info(file=file_id).get('file',{}).get('url_private_download','')

def new_channel_member(channel, user):
    pass

def new_team_member(user):
    pass
