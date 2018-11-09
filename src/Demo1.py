#!coding:utf8

'''
Date:2018/11/9/9:11
Author:yqq
Description: 谷歌翻译的demo
'''

# 请在  File >> Setting >> Project:TranslateTool >> Interpreter >> 设置为 Python3.*

import time
from lib.GoogleTk import Py4Js               #calculate  Tk Value for text
from lib.GoogleTrans import Translate       # tranlate iterface



def main():

	startTime = time.time()
	js = Py4Js()

	with open('../txt/text.txt', 'r') as inputFile :
		allLines = inputFile.readlines()
		for singleLine in allLines:
			rawText = singleLine.strip()  #原文本
			resultText = Translate(rawText, "en", "zh-CN", js.getTk(rawText)) #翻译后的文本
			rawText = rawText.replace('\n', '')
			print(rawText.strip(), "--->", resultText.strip())  # 输出结果
	pass

	endTime = time.time()

	print("========================")
	print("总用时: %.2f s" % (endTime - startTime))



if __name__ == "__main__":

	main()

	pass