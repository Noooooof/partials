@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
cd E:\Recent\MyBlog\source\_update && python updated.py
echo Essays formatted.
echo.
hexo clean && hexo g && hexo s
echo Blog updated.
echo.
pause