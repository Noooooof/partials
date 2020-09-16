@echo off
E:
rd E:\Recent\MyBlog\source\_partials\Theme /s /q
xcopy E:\Recent\MyBlog\themes\hexo-theme-white-master E:\Recent\MyBlog\source\_partials\Theme\ /s /e /q
git add .
git status -s
git commit -m "easy-update"
git push
pause