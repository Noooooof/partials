@echo off
E:
python E:\Recent\MyBlog\source\_partials\Image\Wordcloud\cloud.py
rd E:\Recent\MyBlog\source\_partials\Theme /s /q
xcopy E:\Recent\MyBlog\themes\hexo-theme-white-master E:\Recent\MyBlog\source\_partials\Theme\ /s /e /q
rd E:\Recent\MyBlog\source\_partials\Blog_update /s /q
xcopy E:\Recent\MyBlog\source\_update E:\Recent\MyBlog\source\_partials\Blog_update\ /s /e /q
git add .
git status -s
git commit -m "easy-update"
git push
pause