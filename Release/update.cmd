@echo off
E:
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo d && cd update && python deploy.py
