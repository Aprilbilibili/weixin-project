# coding:utf8
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

import sp_main


import urllib
import urllib2
import json
import sys
reload(sys)
sys.setdefaultencoding('utf8')
	
def test(request):
	obj_spider = sp_main.SpiderMain()
	json_response = obj_spider.craw()
	return HttpResponse(json.dumps(json_response,ensure_ascii=False),content_type='application/json')	
	