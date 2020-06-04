import random
from flask import Flask, request
from pymessenger.bot import Bot
import praw

app = Flask(__name__)
ACCESS_TOKEN = "EAAE8pCfCOWABAKOvZCggxQ4Bed6lHJMhlTjmQBvezqCPqcsf0Gws5gMskvXrjvsVUE4MdsZB59UD8uQ32F777xilKe10Xw1URi2bzZAWxOa3Bh8QR0mAERhHbeaAc2dHuuyMEvq4sZB5G70OtV6IVPw69clvPFHgz6aftEd43eMCtto2mpEoIMHOduKfVf8ZD"
VERIFY_TOKEN = "verifyme"
bot = Bot(ACCESS_TOKEN)
reddit = praw.Reddit(client_id='4VzVtV1hOyiQfg', \
                     client_secret='58gBXfSk5KUaDdoLQ1XTn_Y5-O4', \
                     user_agent='contentmaker', \
                     username='Ermegr', \
                     password='tujh240157')
subreddit = reddit.subreddit('Meme')


@app.route("/", methods=['GET', 'POST'])
def receive_message():
    if request.method == 'GET':
        token_sent = request.args.get("hub.verify_token")
        return verify_fb_token(token_sent)
    else:
       output = request.get_json()
       for event in output['entry']:
           messaging = event['messaging']
           for message in messaging:
               if message.get('message'):
                   recipient_id = message['sender']['id']
                   if message['message'].get('text'):
                       response_sent_text = ''
                       for i in subreddit.top(limit=2):
                           response_sent_text += i.title + '\n'
                           response_sent_text += i.url + '\n'
                           send_message(recipient_id, response_sent_text)
                   if message['message'].get('attachments'):
                       for i in subreddit.top(limit=2):
                           response_sent_text += i.title + '\n'
                           response_sent_text += i.url + '\n'
                           send_message(recipient_id, response_sent_text)

    return "Message Processed"


def verify_fb_token(token_sent):
    if token_sent == VERIFY_TOKEN:
        return request.args.get("hub.challenge")
    return 'Invalid verification token'


def send_message(recipient_id, response):
    bot.send_text_message(recipient_id, response)
    return "success"


if __name__ == "__main__":
    app.run(debug='on')
