#!coding:utf8

'''
Date:2017/8/11/9:40
Lastest update time: 2018/11/08  17:29   update by yqq
Author:yqq
Email: youngqccn@163.com
Github: https://github.com/youngqqcn


Description: 
		注意: 仅支持Python3,  不支持python2 

		only for python3 , not support python2

		ONLY FOR PYTHON3  , NOT SUPPORT PYTHON2!!

'''


import time
from lib.GoogleTk import Py4Js               #calculate  Tk Value for text
from lib.GoogleTrans import Translate       # tranlate iterface


def main():

	js = Py4Js()

	# 法语翻译成中文
	# text = "bonjour"
	# print(Translate(text, "fr", "zh-CN", js.getTk(text)))
	#
	# # 英文翻译成中文
	# text2 = "This is ShenZhen,China."
	# print(Translate(text2, "en", "zh-CN", js.getTk(text2)))
	#
	#
	# # 德语直接翻译成中文
	# text3 = "hallo"
	# print(Translate(text3, "de", "zh-CN", js.getTk(text3)))
	#
	#
	# # 推荐: 先将德文翻译成英文, 再将英文翻译成中文
	# text4 = "hallo"   #德文
	# enText = Translate(text4, "de", "en", js.getTk(text4))
	# print(enText)
	# cnText = Translate(enText, "en", "zh-CN", js.getTk(enText))
	# print(cnText)

	startTime = time.time()

	print('==============================')
	text = "你好,我来自中国.今天天气很好."    # in Chinese means "Hello, I'm from China. The weather is good today."

	print("中文繁体:", Translate(text, "zh-CN", "zh-TW", js.getTk(text)))  #转为繁体   to Tranditional Chinese
	print("英语:", Translate(text, "zh-CN", "en", js.getTk(text))) #翻译为英语    Chinese to  English
	print("法语:", Translate(text, "zh-CN", "fr", js.getTk(text))) #翻译为法语   Chinese to Franch
	print("德语:", Translate(text, "zh-CN", "de", js.getTk(text))) #翻译为德语   Chinese to Detuch
	print("意大利语:", Translate(text, "zh-CN", "it", js.getTk(text))) #翻译为意大利语   Chinese to Italian
	print("阿拉伯语:", Translate(text, "zh-CN", "ar", js.getTk(text))) #翻译为阿拉伯语   Chinese to Arabic
	print("泰语:", Translate(text, "zh-CN", "th", js.getTk(text))) #翻译为泰语
	print("日语:", Translate(text, "zh-CN", "ja", js.getTk(text)))  #翻译为日语   Chinese to Japanese
	print("韩语:", Translate(text, "zh-CN", "ko", js.getTk(text))) #翻译为韩语    Chinese to Korean
	print("西班牙语:", Translate(text, "zh-CN", "es", js.getTk(text))) #翻译为西班牙语   Chinese to Spanish
	print("葡萄牙语:", Translate(text, "zh-CN", "pt", js.getTk(text))) #翻译为葡萄牙语
	print("普什图语:", Translate(text, "zh-CN", "ps", js.getTk(text))) #翻译为普什图语
	print("拉丁语:", Translate(text, "zh-CN", "la", js.getTk(text))) #翻译为拉丁语
	print("马来语:", Translate(text, "zh-CN", "ms", js.getTk(text))) #翻译为马来语(马来西亚语)

	endTime = time.time()
	print("===========================")
	print("Total use: %.2f s" % (endTime  - startTime))
	pass


if __name__ == "__main__":

	main()

	pass


