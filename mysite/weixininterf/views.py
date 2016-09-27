#ckages-*- coding:utf-8 -*-
import sys
import os
os.environ['PYTHON_EGG_CACHE'] = '/tmp/.python-eggs'
reload(sys)
sys.setdefaultencoding('utf8')
from django.http.response import HttpResponse, HttpResponseBadRequest
from django.views.decorators.csrf import csrf_exempt
from wechat_sdk import WechatConf
from wechat_sdk import WechatBasic
from wechat_sdk.exceptions import ParseError
from wechat_sdk.messages import (TextMessage, VoiceMessage, ImageMessage, VideoMessage, LinkMessage, LocationMessage, EventMessage, ShortVideoMessage)
conf = WechatConf(
   token='liuifweixintest',
   appid='wx626bd08fb9ad1e9e',
   appsecret='658b881ac10027877224f288940dc78d',
   encrypt_mode='normal',
   encoding_aes_key=''
)
@csrf_exempt
def wechat_home(request):
   signature = request.GET.get('signature')
   timestamp = request.GET.get('timestamp')
   nonce = request.GET.get('nonce')
   wechat_instance = WechatBasic(conf=conf)
   if not wechat_instance.check_signature(signature=signature, timestamp=timestamp, nonce=nonce):
       return HttpResponseBadRequest('Verify Failed')
   else:
       if request.method == 'GET':
           response = request.GET.get('echostr', 'error')
       else:
           try:
               wechat_instance.parse_data(request.body)
               message = wechat_instance.get_message()
               if isinstance(message, TextMessage):
                   reply_text = 'http://123.206.8.219/query/'
               elif isinstance(message, VoiceMessage):
                   reply_text = '13020031069 liutianfeng'
               elif isinstance(message, ImageMessage):
                   reply_text = '13020031069 liutianfeng'
               elif isinstance(message, LinkMessage):
                   reply_text = '13020031069 liutianfeng'
               elif isinstance(message, LocationMessage):
                   reply_text = '13020031069 liutianfeng'
               elif isinstance(message, VideoMessage):
                   reply_text = '13020031069 liutianfeng'
               elif isinstance(message, ShortVideoMessage):
                   reply_text = '13020031069 liutianfeng'
               else:
                   reply_text = '13020031069 liutianfeng'
               response = wechat_instance.response_text(content=reply_text)
           except ParseError:
               return HttpResponseBadRequest('Invalid XML Data')
       return HttpResponse(response, content_type="application/xml")

