@echo off
E:
cd E:\Recent\MyBlog
set /p var=type: 
hexo new -p %var%%date:~0,4%%date:~5,2%%date:~8,2% "" && cd E:\Recent\MyBlog\source\_posts && %var%%date:~0,4%%date:~5,2%%date:~8,2%.md