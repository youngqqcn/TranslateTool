#!coding:utf8

'''
Date:2018/11/9/11:21
Author:yqq
Description: 百度翻译
'''

# 请在  File >> Setting >> Project:TranslateTool >> Interpreter >> 设置为 Python2.7.*


import sys
import time
from lib.BDtraslate import Translate

#reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':
	with open('../txt/text.txt', 'r') as inputFile:
		allLines = inputFile.readlines()
		for singleLine in allLines:
			rawText = singleLine.strip()  # 原文本
			resultText = Translate(rawText, "en", "zh")  # 翻译后的文本
			print(rawText),
			print("-->"),
			print(resultText)  # 输出结果
		pass
	pass