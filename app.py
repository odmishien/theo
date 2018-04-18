from flask import Flask, request, abort
from flask.ext.sqlalchemy import SQLAlchemy
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
line_bot_api = LineBotApi('6w+yDVbtosggFA+eHjGvxbdxvtiNnbo2Szpet/7pvsF2VIoNpMR29zVUGCKnheQdBWJBWk1hnNVc2UIjooUdn/vbDm6pHU2EZkG9gUXdjPkoeVUIePuKqipmQYExGPlKeQxYIVv1oU6wbtQXjMBR5gdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('9ae6932fad2fa65e7020d34b3d41d2a2')

#DB接続部分
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
db = SQLAlchemy(app)

class Ids(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    groupid = db.column(db.String(50)) 
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

@handler.add(MessageEvent)
def shiyoya(event):
    groupid = event.source.user_id
    print(groupid)
    if not db.session.query(Ids).filter(Ids.groupid == groupid).count():
        reg = Ids(groupid)
        db.session.add(reg)
        db.session.commit()
if __name__ == '__main__':
    app.run()