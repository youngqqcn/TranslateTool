#!coding:utf8

'''
Author:yqq
Date:  2017-6
Descriptions: 自动识别语言种类, 
			  仅支持python2, python3会报编码异常
			  
			  Auto detect text language, eg: if you input Chinese text , 
			  this tool will tell you text's language is Chinese
              only for python2
              python3 will raise decode error, such as 
              "'gbk' codec can't decode byte ..."
'''

#如果没有安装langid , 请为python2安装 langid
#if not installed `langid` , please install `langid` by `pip install langid` for python2
import langid


def DetectLanguage(inText):

	lineTuple = langid.classify(inText)  #
	print(lineTuple)
	pass


def main():


	DetectLanguage("你好,世界")  # ouput ('zh',..)  , Simplify Chinese, 中文简体
	DetectLanguage("中國長城萬里長,龍的傳人")  # ouput ('zh', ...)  , Traditional Chinese , 中文繁体
	DetectLanguage("Hello, I am from China. The weather is very good today.")  # ouput ('en', ...) , English 英语
	DetectLanguage("Bonjour, je viens de Chine et il fait très beau aujourd'hui.")  # ouput ('fr',...) , Franch  法语
	DetectLanguage("Hallo, ich komme aus China, das Wetter ist heute sehr gut.")  # ouput('de',..) Detuch  德语
	DetectLanguage("Ciao, vengo dalla Cina, il tempo è molto buono oggi.")  # ouput('it', ...) Italian 意大利语
	DetectLanguage("مرحباً ، أنا من الصين ، الطقس جيد جداً اليوم")  # ouput ('ar', ...) Arabic  阿拉伯语
	DetectLanguage("안녕하세요, 저는 중국 출신입니다. 오늘은 날씨가 아주 좋습니다.")  # ouput('ko', ..)  Korean  韩语
	DetectLanguage("سلام، زه د چين يم. نن ورځ ښه ده")  # ouput ('ps', ...)  Pashto  普什图语
	DetectLanguage("こんにちは、私は中国出身です。今日は天気がとても良いです。")  # ouput ('ja',.. ) Janpanese 日语
	DetectLanguage("สวัสดีฉันมาจากประเทศจีนอากาศดีมากในวันนี้")  # ouput ('th',...) 泰语


	pass


if __name__ == '__main__':
	main()
	pass