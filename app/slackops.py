# Author: Aleem Juma

def send_reply(client, user, message):
    client.chat_postMessage(
        channel='D01BDH7USJH',
        blocks=[
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': f'*{user}* mentioned me, saying:'
                }
            },
            {
                'type': 'divider',
            },
            {
                'type': 'section',
                'text': {
                    'type': 'mrkdwn',
                    'text': message
                }
            },
            {
                'type': 'divider',
            },
        ]
    )
