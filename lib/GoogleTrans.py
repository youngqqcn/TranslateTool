#coding:utf8



#  only for python3


import urllib.request
from lib.GoogleTk import Py4Js
from lib.GoogleTk import gUserAgent
import sys
import random

gContent = [
"bonjour",
]


'''
#以下是目前支持的语言, 可以自行增加
#Below is all language be support by current version, also you can add other language by yourself.

zh-CN:中文简体    Simplify Chinese
zh-TW:中文繁体   Tranditional Chinese
en:英语    English
fr:法语    Franch
ja:日语    Japanese
de:德语    Detuch
ar:阿拉伯语  Arabic
pt:葡萄牙语   Portuguese
ru:俄语        Rusia
it:意大利语    Italian
es:西班牙语  Español   Spanish
ko:韩语     Korean
fa:波斯语    Farsi
th:泰语     Thai 
vi:越南语   Vietnamese
pl:波兰语   Polish
ps:普什图语  Pashto
el:希腊语    Greek
id:印尼语   Indonesian
ms:马来语   Malay
la:拉丁语   Latin
nl:荷兰语   Dutch
fi:芬兰语  Finnish
'''

gLanguage = ["en", "zh-CN", "zh-TW", "fr", "de", "ja", "ar", "pt", "ru", \
             "it", "es", "ko", "fa", "fa", "th", "vi", "pl", "ps",\
             "el", "el", "id", "ms", "la", "nl", "fi"]

def OpenURL(url):
	'''
	:param url: 组装好的URL(包含了原语种,目标语种,tk值) , this url to request google server
	:return: 返回谷歌翻译后的文本,以UTF-8编码,  the result text return by google
	'''
	headers = {'User-Agent': gUserAgent[random.randint(0, len(gUserAgent)-1)]}
	req = urllib.request.Request(url=url, headers=headers)
	response = urllib.request.urlopen(req)
	data = response.read().decode('utf-8')
	return data


def Translate(content, srcLan, dstLan, tk):
	'''
	:param content: 待翻译的内容 , the text be translate
	:param srcLan: 原语种  , source language
	:param dstLan: 目标语种,  destination language
	:param tk: Google的tk值, the tk value for text
	:return: 翻译后的文本 , the result text
	'''

	if (srcLan not in gLanguage):
		print("srcLan is not supported!")
		return
	if (dstLan not in gLanguage):
		print("dstLan is not supported!")
		return

	if len(content) > 4891:
		print("content is too long!")
		return

	content = urllib.parse.quote(content)

	#核心 url
	#most inportant url  to request
	url = "http://translate.google.cn/translate_a/single?client=t" \
	      "&sl={0}&tl={1}&hl=zh-CN&dt=at&dt=bd&dt=ex&dt=ld&dt=md&dt=qca" \
	      "&dt=rw&dt=rm&dt=ss&dt=t&ie=UTF-8&oe=UTF-8&clearbtn=1&otf=1&pc=1" \
	      "&srcrom=0&ssel=0&tsel=0&kc=2&tk={2}&q={3}".format(srcLan, dstLan, tk, content)

	result = OpenURL(url)
	#print(result)

	end = result.find("\",")
	if end > 4:
		#print(result[4 : end])
		return result[4 : end]
	else:
		print("ERROR")
		return "ERROR"



