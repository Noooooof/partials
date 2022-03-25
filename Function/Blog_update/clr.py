# coding:utf-8

import os
import re
import time

path = '../_posts' # _posts文件夹位置

for file in os.listdir(path):
	if ('.md' in file):
		fileName = os.path.join(path,file)
		with open(fileName,'r',encoding="utf-8")as fi:
			postContent = fi.read() # markdown文件内容


		post = postContent # 准备覆写
		'''	
		flagCategoris = re.search(r'categories: \d*\.\d*\n',postContent)
		if (flagCategoris != None):
			post = re.sub(r'categories: \d*\.\d*\n', 'categories: Diary\n', post)
		else:
			flagCategoris = re.search(r'categories: \'\d*\.\d*\'\n',postContent)
			if (flagCategoris != None):
				post = re.sub(r'categories: \'\d*\.\d*\'\n', 'categories: Diary\n', post)
		'''
		postCategoris = re.findall(r'categories: ([\s\S]*?)\n',postContent)[0]
		if ('\'' not in postCategoris):
			post = re.sub(r'categories: ([\s\S]*?)\n', 'categories: \'' + postCategoris + '\'\n', post)
		
		postTags = ""
		if (re.search(r'tags: ([\s\S]*?)\n',postContent)):
			postTags = re.findall(r'tags: ([\s\S]*?)\n',postContent)[0]
		if (postTags=='locked'):
			post = re.sub(r'tags: ([\s\S]*?)\n', 'tags: \'locked\'\n', post)

		if (post != postContent):
			with open(fileName,'w',encoding="utf-8")as fo:
				fo.write(post) # 覆写
