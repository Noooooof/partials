@echo off
color 02
E:
python E:\Recent\MyBlog\source\_update\updated.py
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
pause>nul