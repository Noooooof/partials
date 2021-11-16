@echo off
E:
python E:\Recent\MyBlog\source\_partials\Image\Wordcloud\cloud.py
echo.
echo Wordcloud done.
echo.
cd E:\Recent\MyBlog\source\_update && python updated.py
echo Essays formatted.
echo.
hexo clean && hexo g && hexo s
pause