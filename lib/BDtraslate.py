#coding:utf8
import sys
import httplib
import md5
import urllib
import random
from time import sleep
'''
语言简写	名称
auto	自动检测
zh	中文
en	英语
yue	粤语
wyw	文言文
jp	日语
kor	韩语
fra	法语
spa	西班牙语
th	泰语
ara	阿拉伯语
ru	俄语
pt	葡萄牙语
de	德语
it	意大利语
el	希腊语
nl	荷兰语
pl	波兰语
bul	保加利亚语
est	爱沙尼亚语
dan	丹麦语
fin	芬兰语
cs	捷克语
rom	罗马尼亚语
slo	斯洛文尼亚语
swe	瑞典语
hu	匈牙利语
cht	繁体中文
vie	越南语

'''

reload(sys)
sys.setdefaultencoding('utf-8')

gAppid = '20151113000005349'
gSecretKey = 'osubCEzlGjzvw8qdQc41'
gURL = '/api/trans/vip/translate'


def Translate(qWord, srcLan, dstLan):
	'''
	:param qWord: 要翻译的字符串,  the text to be translate
	:param srcLan: 原语种 , source language
	:param dstLan: 目标语种, destination language
	:return: 翻译完成的语种, 失败返回"TRANS_ERROR" ,    the result text , if failed return "TRANS_ERROR"
	'''

	httpClient = None
	#q = 'failure to control nozzle cylinder 4'
	fromLang = srcLan
	toLang = dstLan
	salt = random.randint(32768, 65536)

	sign = gAppid + qWord + str(salt) + gSecretKey
	m1 = md5.new()
	m1.update(sign)
	sign = m1.hexdigest()
	myurl = gURL + '?appid=' + gAppid + '&q=' + \
	        urllib.quote(qWord) + '&from=' + fromLang + \
	        '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + sign

	try:
		httpClient = httplib.HTTPConnection('api.fanyi.baidu.com')
		httpClient.request('GET', myurl)

		# response是HTTPResponse对象
		# response is HTTPResponse's  object
		response = httpClient.getresponse()
		retStr = response.read()
		uStr = retStr[retStr.find("dst") + 6: -4]

		#休眠一秒降低请求频率,防止百度返回54003错误,
		# sleep 1 second , to avoid 54003 error which is "request too frequently".
		sleep(1)
		return uStr.decode("unicode_escape")
	except Exception, e:
		print e
		return "TRANS_ERROR"
	finally:
		if httpClient:
			httpClient.close()

	pass
