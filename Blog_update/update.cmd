@echo off
E:
cd E:\Recent\MyBlog\source\_update && python updated.py
cd E:\Recent\MyBlog
start chrome.exe https://gitee.com/Noooooof/Noooooof/pages
hexo clean && hexo g && hexo d
pause