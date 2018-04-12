from app import groups
from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent,JoinEvent, TextMessage, TextSendMessage,ImageMessage,ImageSendMessage,TemplateSendMessage,ConfirmTemplate,PostbackTemplateAction,MessageTemplateAction
)
for id in groups:
    # num = random.randrange(30)
    # if num < 2:
    line_bot_api.push_message(id,TemplateSendMessage(
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
        )))
print(groups)