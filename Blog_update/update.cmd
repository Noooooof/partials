@echo off
E:
cd E:\Recent\MyBlog\source\_partials
call de_git.bat
cd E:\Recent\MyBlog\source\_update && python updated.py
echo 文件处理完成......
echo.
hexo clean && hexo g && hexo s
echo 博客上传完成......
echo.
pause