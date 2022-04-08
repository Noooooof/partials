@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo d
pause>nul