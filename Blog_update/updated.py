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

		localDate = time.strftime("%Y-%m-%d", time.localtime()) # 当前时间
		localUpdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(fileName).st_mtime)) # 文件修改时间
		
		postCategoris = re.findall(r'categories: ([\s\S]*?)\n',postContent)[0] # 分类
		postDate = re.findall(r'date: ([\s\S]*?)\n',postContent)[0] # date时间
		postUpdate = re.findall(r'updated: ([\s\S]*?)\n',postContent)[0] # update时间

		post = "" # 准备覆写

		if (localDate not in localUpdate): # 过往文章
			if (postDate != postUpdate):
				post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postDate +'\n', postContent) # 按date时间复位
		else:
			if (localDate in postUpdate): # 今日更新文章
				if ((postCategoris != '\'Diary\'') and (postDate != postUpdate)):
					post = re.sub(r'date: [\s\S]*?\n','date: '+ postUpdate +'\n', postContent) # 连载按update时间更新date时间
		
		if (post):
			with open(fileName,'w',encoding="utf-8")as fo:
				fo.write(post) # 覆写
