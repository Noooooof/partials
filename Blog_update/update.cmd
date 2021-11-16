@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
cd E:\Recent\MyBlog\source\_update && python updated.py
echo.
hexo clean && hexo g && hexo s
pause