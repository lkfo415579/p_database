#coding:utf-8
import uniout
import MySQLdb

host = "127.0.0.1"
global db
global dbc
db = MySQLdb.connect(host=host, user='lkfo', passwd='qq321520', db='pixiv')
db.set_character_set('utf8')
dbc= db.cursor()
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')

import cPickle as pickle

def Title_Tags():
	sys_sql = "select title,tags from pictures"
	print (sys_sql)
	dbc.execute(sys_sql)
	result = dbc.fetchall()
	dbc.close()
	return result
	
	
	
data = Title_Tags()
new_data = []
for node in data:
	
	tmp = [str[1:-1] for str in node[1][1:-1].split(",")]
	new_data.append([node[0],tmp])
	
print type(new_data[0][0])
print new_data[0][0]
print type(new_data[0][1])
print new_data[0][1]
for tag in new_data[0][1]:
	print tag
print "Structure: [id][0=name,1=tags]"
pickle.dump( new_data, open( "TITLE_TAGS.p", "wb" ) )