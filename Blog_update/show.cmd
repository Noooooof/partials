@echo off
E:
start Chrome.exe http://localhost:4000
cd E:\Recent\MyBlog\source\_update && python updated.py
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo s