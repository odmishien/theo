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

TOKEN = os.environ(['TOKEN'])
line_bot_api = LineBotApi(TOKEN)

ids = Ids.query.all()
for id in ids:
    num = random.randrange(30)
    if num < 2:
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
