# coding:utf-8

import os
import re
import time

path = '../_posts'

for file in os.listdir(path):
	if ('.md' in file):
		fileName = os.path.join(path,file)
		with open(fileName,'r',encoding="utf-8")as fi:
			postContent = fi.read()

		localDate = time.strftime("%Y-%m-%d", time.localtime()) 
		localUpdate = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(os.stat(fileName).st_mtime))
		
		postCategoris = re.search(r'categories: \d*\.\d*\n',postContent)
		if (postCategoris == None):
			postCategoris = re.search(r'categories: \'\d*\.\d*\'\n',postContent)
		postDate = re.findall(r'date: ([\s\S]*?)\n',postContent)[0]		
		postUpdate = re.findall(r'updated: ([\s\S]*?)\n',postContent)[0]
		post = postContent
		if (localDate in localUpdate):
			postUpdate = localUpdate
			post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postUpdate +'\n', post)
			if (postCategoris == None):
				post = re.sub(r'date: [\s\S]*?\n','date: '+ postUpdate +'\n', post)
		else:		
			post = re.sub(r'updated: [\s\S]*?\n','updated: '+ postDate +'\n', post)
			
		with open(fileName,'w',encoding="utf-8")as fo:
			fo.write(post)
		

