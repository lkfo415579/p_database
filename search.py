#coding:utf-8
import uniout
import MySQLdb
from database import config
global db
global dbc
db = MySQLdb.connect(host=config.host, user='lkfo', passwd='qq321520', db='pixiv')
db.set_character_set('utf8')
dbc= db.cursor()
dbc.execute('SET NAMES utf8;')
dbc.execute('SET CHARACTER SET utf8;')
dbc.execute('SET character_set_connection=utf8;')

def images(result):
	#16 image_files_name
	list = []
	for record in result:
		list.append(record[16])
	return list

def Main_database_search(token):
	token_condition = ""
	for x in range(len(token)):
		if (x >0 and x < len(token)):
			token_condition = token_condition + " and "
		tmp_key = '%s' % token[x]
		token_condition = token_condition + "(title LIKE '%"+tmp_key+"%' or tags LIKE '%"+tmp_key+"%')"
		#token_condition = token_condition + "(tags LIKE '%"+tmp_key+"%')"
	
	sys_sql = "select * from pictures where " + token_condition
	print (sys_sql)
	dbc.execute(sys_sql)
	result = dbc.fetchall()
	return result
	
def copyFile(src, dest):
	import shutil
	try:
		shutil.copy(src, dest)
	# eg. src and dest are the same file
	except shutil.Error as e:
		print('Error: %s' % e)
	# eg. source or destination doesn't exist
	except IOError as e:
		print('Error IO: %s' % e.strerror)
	
def move(files_list):
	#####
	directory = "search/"
	import shutil
	shutil.rmtree(directory)
	import os
	if not os.path.exists(directory):
		os.makedirs(directory)
	for file in files_list:
		new_file = file.split('/')[0]+'-'+file.split('/')[1]
		if not (os.path.isfile(directory+new_file)):
			print new_file
			copyFile(file,directory+new_file)
	#####
	print "Total found : %s" % str(len(files_list)-1)
	#####
	
if __name__ == '__main__':
	import sys
	token = []
	for x in range(1,len(sys.argv)):
		token.append(sys.argv[x])
	#token = '艦これ'
	#token = '甲鉄城'
	#token = '無名'
	result = Main_database_search(token)
	files_list = images(result)
	move(files_list)
	dbc.close()