@echo off
E:
cd E:\Recent\MyBlog
start chrome.exe https://gitee.com/Noooooof/Noooooof
hexo clean && hexo g && hexo d
pause