@echo off
E:
cd E:\Recent\MyBlog\source\_partials\Font\fontspider
call spider.cmd
cd E:\Recent\MyBlog\source\_partials
git add .
git status -s
git commit -m "easy-update"
git push
pause