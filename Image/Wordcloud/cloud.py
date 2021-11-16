# coding:utf-8

import os
import re
import jieba
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

postPath = 'E:/Recent/MyBlog/source/_posts' # _posts文件夹位置
fontPath = 'E:/Recent/MyBlog/source/font/H-GUNGSEO2.2.ttf' # 字体文件位置
path = os.path.dirname(__file__) # 所在文件夹位置

def clearFile(content):
	fileContent = ""
	contentClrHead = re.sub(r'^---\n([\s\S]*?)\n---',"",content)
	contentClrLine = re.sub(r'<br>',"",contentClrHead)
	contentClrCode = re.sub(r'```\n([\s\S]*?)\n```',"",contentClrLine)
	contentClrHtml = re.sub(r'\[([\s\S]*?)\]\(http.*\)',"",contentClrCode)
	contentClrFormat = re.sub(r'[#*>\s`]',"",contentClrHtml)
	fileContent = contentClrFormat
	return fileContent

def scanFile(path):
	text = ""
	filelist = os.listdir(path)
	for filename in filelist:
		filepath = os.path.join(path,filename)
		if os.path.isdir(filepath):
			if re.match(r'[_\.]',filename):
				pass
			else:
				text += scanFile(filepath)
		else:
			with open(filepath,'r',encoding="utf-8")as fi:
				text += clearFile(fi.read())
	return text

def clearName(content):
	namelist = ['远山有灯','斯丢匹德做个人吧','岸边渡鸦','余娱余愚','Nof','君子不器','NULL','Prisoner24601','咩','斯丢匹德是个废物','插兜','斯丢匹德扑棱扑棱','斯丢匹德']
	for name in namelist:
		content = re.sub(name,'',content)
	return content

def creatCloud(result):
	# 分词
	wordList = jieba.lcut(result) 

	# 去除停用词
	fileRemove = os.path.join(path,'banlist.txt')
	with open(fileRemove,'r',encoding="utf-8")as fr:
		content = fr.read()
	removeList = re.findall('.+',content)

	# 词频统计
	objectList = []
	for word in wordList:
		if word not in removeList:
			objectList.append(word)
	wordCounts = collections.Counter(objectList)

	# 生成词云
	backPath = os.path.join(path, 'background.jpg')
	coloring = np.array(Image.open(backPath))
	imageColors = ImageColorGenerator(coloring)


	wordCloud = WordCloud(background_color ="white",max_words = 1000,mask=coloring, color_func=imageColors, max_font_size=96,random_state=42, scale=3,font_path = fontPath).generate_from_frequencies(wordCounts)
	wordCloud.to_file(os.path.join(path,'blog.png'))
	'''
	plt.imshow(wordCloud)
	plt.axis('off')
	plt.show()
	'''

postContent = scanFile(postPath)
creatCloud(clearName(postContent))
print('Wordcloud has been built successfully.\n')