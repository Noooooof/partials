@echo off
E:
cd E:\Recent\MyBlog\source\_update && python updated.py
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo d && cd E:\Recent\MyBlog\source\_update && python deploy.py
pause