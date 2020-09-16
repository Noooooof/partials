@echo off
E:
cd E:\Recent\MyBlog\source\_partials\Font\fontspider
call spider.cmd
Xcopy E:\Recent\MyBlog\source\_partials\Font\H-TTF-BuMing-R-2.ttf E:\Recent\MyBlog\themes\hexo-theme-white-master\source\font /Y
cd E:\Recent\MyBlog\source\_partials
git add .
git status -s
git commit -m "easy-update"
git push
pause