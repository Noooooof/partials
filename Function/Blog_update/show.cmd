@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
color 08
cd E:\Recent\MyBlog
start chrome.exe  http://localhost:4000
hexo clean && hexo g && hexo s
pause>nul