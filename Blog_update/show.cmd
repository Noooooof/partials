@echo off
E:
cd E:\Recent\MyBlog\source\_update && python updated.py
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo s && start C:\Users\Black\AppData\Local\Google\Chrome\Application\chrome.exe http://localhost:4000