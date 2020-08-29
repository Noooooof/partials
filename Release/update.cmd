@echo off
E:
cd E:\Recent\MyBlog\source\_partials\Image\Wordcloud
python oper.py
cd E:\Recent\MyBlog\source\_partials
call update.cmd
cd E:\Recent\MyBlog
hexo clean && hexo g && hexo d && cd E:\Recent\MyBlog\source\_partials\Release && python deploy.py
