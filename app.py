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

@handler.add(MessageEvent)
def shiyoya(event):
    Id = event.source.user_id
    print(Id)
    f = open("/tmp/ids.txt",'a')
    f.write(str(Id) + "\n")
    f.close()

if __name__ == '__main__':
    app.run()