@echo off
E:
cd E:\Recent\MyBlog
start chrome.exe http://localhost:4000
hexo clean && hexo g && hexo s