# coding:utf-8

import os
import re
import jieba
import collections
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
import numpy as np
import PIL.Image as Image

postPath = '../../../_posts' # _posts文件夹位置
fontPath = '../../Font/H-TTF-BuMing-R-2.ttf' # 字体文件位置
path = os.path.dirname(__file__) # 所在文件夹位置

def clearFile(content):
	fileContent = ""
	if (content.find("tags: silly") == -1): # 如果没加密
		contentClrHead = re.sub(r'^---\n([\s\S]*)\n---',"",content)
		contentClrLine = re.sub(r'<br\/>',"",contentClrHead)
		contentClrCode = re.sub(r'```\n([\s\S]*)\n```',"",contentClrLine)
		contentClrFormat = re.sub(r'[#*>\s`]',"",contentClrCode)
		contentClrHtml = re.sub(r'\[([\s\S]*)\]\(http.*\)',"",contentClrFormat)
		fileContent = contentClrHtml
	return fileContent

def getFile(logPath):
	text = ""
	for file in os.listdir(logPath):
		fileInput = os.path.join(logPath,file)
		with open(fileInput,'r',encoding="utf-8")as fi:
			text += clearFile(fi.read())
	return text

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

postContent = getFile(postPath)
creatCloud(postContent)
print('Wordcloud has been built successfully.\n')