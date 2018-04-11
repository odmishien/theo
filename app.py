from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,JoinEvent, TextMessage, TextSendMessage,ImageMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,PostbackTemplateAction,MessageTemplateAction
)
import datetime
import sched
import time

app = Flask(__name__)

line_bot_api = LineBotApi('6w+yDVbtosggFA+eHjGvxbdxvtiNnbo2Szpet/7pvsF2VIoNpMR29zVUGCKnheQdBWJBWk1hnNVc2UIjooUdn/vbDm6pHU2EZkG9gUXdjPkoeVUIePuKqipmQYExGPlKeQxYIVv1oU6wbtQXjMBR5gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9ae6932fad2fa65e7020d34b3d41d2a2')

@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return ''

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="月に2回、突然飲み会セッティングするからよろしく頼むわ！！"))
@handler.add(JoinEvent)
def shiyoya(event):
    scheduler = sched.scheduler(time.time, time.sleep)
    scheduler.enter(10,1,line_bot_api.reply_message(
        event.reply_token,
        TemplateSendMessage(
            alt_text='Confirm template',
            template=ConfirmTemplate(
            text='明日、飲み会しよや！！',
            actions=[
            PostbackTemplateAction(
                label='アリ',
                text='アリ',
                data='action=buy&itemid=1'
            ),
            MessageTemplateAction(
                label='ナシ',
                text='ナシ'
            )
        ]
    )
)))
    
    
if __name__ == '__main__':
    app.run()