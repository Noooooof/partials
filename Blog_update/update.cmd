@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
echo.
echo Files updated.
echo.
cd E:\Recent\MyBlog\source\_update && python updated.py
echo Essays formatted.
echo.
hexo clean && hexo g && hexo s
pause