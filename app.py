from flask import Flask, request, abort
from flask_sqlalchemy import SQLAlchemy
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,JoinEvent, TextMessage, TextSendMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,PostbackTemplateAction,MessageTemplateAction
)
import os

app = Flask(__name__)
TOKEN = os.environ(['TOKEN')
HANDLER = os.environ(['HANDLER'])
line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(HANDLER)

#DB接続部分
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Ids(db.Model):
    __tablename__  = "ids"
    id = db.Column(db.Integer,primary_key=True)
    groupid = db.Column(db.String(),nullable=False) 
    def __init__(self, groupid):
        self.groupid = groupid
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

@handler.add(JoinEvent)
def shiyoya(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="月に2〜5回ランダムで突然飲みたがります！どうぞよろしく！！"))
    groupid = event.source.group_id
    reg = Ids(groupid)
    db.session.add(reg)
    db.session.commit()
if __name__ == '__main__':
    app.run()
