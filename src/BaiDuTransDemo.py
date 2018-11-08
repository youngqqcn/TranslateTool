#coding:utf8


#百度翻译接口,  Baidu  translate
# 请使用  python2 ,  Please use python2

import sys
import time
from lib.BDtraslate import Translate

#reload(sys)
sys.setdefaultencoding('utf-8')


if __name__ == '__main__':

	print(Translate("我来自中国", "zh", "en"))
	print(Translate("我来自中国", "zh", "it"))
	print(Translate("สวัสดีฉันมาจากประเทศจีนอากาศดีมากในวันนี้", "th", "zh"))
	pass
