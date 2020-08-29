@echo off
E:
cd E:\Recent\MyBlog
hexo new -p d%date:~0,4%%date:~5,2%%date:~8,2% "" && cd E:\Recent\MyBlog\source\_posts && d%date:~0,4%%date:~5,2%%date:~8,2%.md