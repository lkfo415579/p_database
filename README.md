License
------
pixiv API fork from https://github.com/upbit/pixivpy
DATABASE_PIXIV
-------------
3.2version
Done,basic achitecture of database of pixiv
Usage:
-------------
1. setup database config and pixiv ac in database/config.py (default databasename : pixiv)
2. "pixiv.sql" is a demo database structure, import it to mysql
3. python database.py -h

PS:
------
Usage:python database.py [year=2015] [month=1] [per_page=20]
it will start from year 2015 month 1 , then save images into relative current path folder.
if you want to change the category , you need to edit database.py.
