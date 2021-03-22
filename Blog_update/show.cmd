@echo off
E:
start C:\Users\Black\AppData\Local\Google\Chrome\Application\chrome.exe http://localhost:4000
cd E:\Recent\MyBlog\source\_update && python updated.py
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo s