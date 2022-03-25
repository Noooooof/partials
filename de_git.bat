@echo off
E:
python E:\Recent\MyBlog\source\_update\updated.py
rd E:\Recent\MyBlog\source\_posts /s /q
xcopy "E:\Recent\OneDrive - pku.edu.cn\Note\Blog" E:\Recent\MyBlog\source\_posts\ /s /e /q
python E:\Recent\MyBlog\source\_partials\Function\Wordcloud\cloud.py
rd E:\Recent\MyBlog\source\_partials\Theme /s /q
xcopy E:\Recent\MyBlog\themes\hexo-theme-white-master E:\Recent\MyBlog\source\_partials\Theme\ /s /e /q
rd E:\Recent\MyBlog\source\_partials\Function\Blog_update /s /q
xcopy E:\Recent\MyBlog\source\_update E:\Recent\MyBlog\source\_partials\Function\Blog_update\ /s /e /q
git add .
git status -s
git commit -m "easy-update"
git push
echo.
echo Files updated.
echo.
pause