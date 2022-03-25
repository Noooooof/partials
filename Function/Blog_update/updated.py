# coding:utf-8

import os
import re
import time

postpath = 'E:/Recent/MyBlog/source/_posts' # _posts文件夹位置

def oper(tag,fileName):
	with open(fileName,'r',encoding="utf-8")as fi:
		postContent = fi.read() # markdown文件内容

	post = postContent # 准备覆写
	flag = 0

	postCategoris = re.search(r'categories: ([\s\S]*?)\n',postContent) # 分类
	if (postCategoris.group(1)!=tag):
		flag = 1
		post = re.sub(r'categories: ([\s\S]*?)\n','categories: ' + tag + '\n',post)

	localDate = time.strftime("%Y-%m-%d", time.localtime()) # 当前时间
	postDate = re.findall(r'date: ([\s\S]*?)\n',postContent)[0] # date时间
	postUpdate = re.findall(r'updated: ([\s\S]*?)\n',postContent)[0] # update时间
	if (postDate != postUpdate):
		if (localDate not in postUpdate): # 非new
			flag = 1
			post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postDate +'\n', post) # 按date时间复位
		else: # new post
			if (tag != 'Diary'):
				flag = 1
				post = re.sub(r'date: [\s\S]*?\n','date: '+ postUpdate +'\n', post) # 连载按update时间更新date时间
	
	if (flag):
		with open(fileName,'w',encoding="utf-8")as fo:
			fo.write(post) # 覆写
		print('This file has been rewritten: '+fileName[len(postpath):])

	return

def finddir(tag,path):
	for file in os.listdir(path):
		filepath = os.path.join(path,file)
		if (re.search(r'^[\._]',file)==None):
			if os.path.isdir(filepath):
				finddir(file,filepath)
			else:
				if (re.search(r'\.md$',file)!=None):
					oper(tag,filepath)
	return

finddir('Blog',postpath)
print('\nEssays formatted.\n')