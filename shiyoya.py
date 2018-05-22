from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,JoinEvent, TextMessage, TextSendMessage,ImageMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,PostbackTemplateAction,MessageTemplateAction
)
from flask_sqlalchemy import SQLAlchemy
from app import Ids
import random

line_bot_api = LineBotApi('6w+yDVbtosggFA+eHjGvxbdxvtiNnbo2Szpet/7pvsF2VIoNpMR29zVUGCKnheQdBWJBWk1hnNVc2UIjooUdn/vbDm6pHU2EZkG9gUXdjPkoeVUIePuKqipmQYExGPlKeQxYIVv1oU6wbtQXjMBR5gdB04t89/1O/w1cDnyilFU=')
# signature = request.headers['X-Line-Signature']

# # get request body as text
# body = request.get_data(as_text=True)
# # handle webhook body
# try:
#     handler.handle(body, signature)
# except InvalidSignatureError:
#     abort(400)
ids = Ids.query.all()
for id in ids:
#     num = random.randrange(30)
#     if num < 2:
    line_bot_api.push_message(id.groupid,TemplateSendMessage(
            alt_text='明日、飲み会しよや！！',
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
            )))