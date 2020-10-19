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
		
		postCategoris = re.search(r'categories: \d*\.\d*\n',postContent)
		if (postCategoris == None):
			postCategoris = re.search(r'categories: \'\d*\.\d*\'\n',postContent) # 非None就是日记

		postDate = re.findall(r'date: ([\s\S]*?)\n',postContent)[0] # date时间
		postUpdate = re.findall(r'updated: ([\s\S]*?)\n',postContent)[0] # update时间

		post = postContent # 准备覆写
		
		if (localDate in localUpdate): # 如果是当天修改的文件
			postUpdate = localUpdate
			post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postUpdate +'\n', post) # 更新update时间
			if (postCategoris == None):
				post = re.sub(r'date: [\s\S]*?\n','date: '+ postUpdate +'\n', post) # 连载文章更新date时间
		else:		
			post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postDate +'\n', post) # 以前的文章按date时间复位
			
		with open(fileName,'w',encoding="utf-8")as fo:
			fo.write(post) # 覆写
		

