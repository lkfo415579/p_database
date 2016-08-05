#coding:utf-8
#tar -zcvf /cygdrive/i/pixiv/image_train.tar.gz train
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
import os
def clean_UP():
	import shutil
	try:
		shutil.rmtree('train/')
		shutil.rmtree('val/')
		os.remove("train.txt")
		os.remove("val.txt")
	except:
		pass

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
	#print (sys_sql)
	dbc.execute(sys_sql)
	result = dbc.fetchall()
	return result
	
def copyFile(src, dest):
	import shutil
	try:
		shutil.copy(src, dest)
	# eg. src and dest are the same file
	except shutil.Error as e:
		#print('Error: %s' % e)
		pass
	# eg. source or destination doesn't exist
	except IOError as e:
		#print('Error IO: %s' % e.strerror)
		#print src
		pass
import re
def g_file_name(f):
	folder = f.split('/')
	m = re.search('\((\d+)\)\.', f)
	id = m.group(1)
	fomat = f.split('.')[-1]
	
	return folder[0]+'-'+id+'.'+fomat
	
def move(files_list,directory):
	#####
	#directory = "train/"
	#import shutil
	#shutil.rmtree(directory)

	if not os.path.exists(directory):
		os.makedirs(directory)
	for file in files_list:
		new_file = g_file_name(file)
		if not (os.path.isfile(directory+new_file)):
			#print new_file
			copyFile(file,directory+new_file)
	#####
	print "Total found : %s" % str(len(files_list)-1)
	#####
	
def assign_val(files_list,file_train_list):
	val_list = []
	for file in files_list:
		if not(file in file_train_list):
			val_list.append(file)
	return val_list
	
if __name__ == '__main__':
	import sys
	import random
	clean_UP()
	token = []
	#for x in range(1,len(sys.argv)):
	#	token.append(sys.argv[x])
	
	#reading tag list
	tag_list = []
	with open("synset_words.txt",'r') as file:
		for line in file:
			tag_list.append(line.strip().split(' '))
	##
	file_train_list = []
	file_val_list = []
	print "Starting exporting train&val dataset"
	#tag_info[0] = tagID,tag_info[1] = tag_name
	runing_tag = 0
	for tag_info in tag_list:
		print tag_info[1]
		token = []
		token.append(tag_info[1])
		result = Main_database_search(token)
		files_list = images(result)
		file_train_list = random.sample(files_list, int(len(files_list)*0.85))
		file_val_list = assign_val(files_list,file_train_list)
		move(file_train_list,"train/")
		move(file_val_list,"val/")
		f_t_l_name = [g_file_name(file) for file in file_train_list]
		f_v_l_name = [g_file_name(file) for file in file_val_list]
		with open("train.txt", 'a') as outfile:
			#outfile.writelines([x+" "+tag_info[0] + "\n" for x in f_t_l_name])
			outfile.writelines([x+" "+str(runing_tag) + "\n" for x in f_t_l_name])
		with open("val.txt", 'a') as outfile:
			#outfile.writelines([x+" "+tag_info[0] + "\n" for x in f_v_l_name])
			outfile.writelines([x+" "+str(runing_tag) + "\n" for x in f_v_l_name])
		runing_tag += 1
		#if (runing_tag > 1):
		#	sys.exit()
		
	print "End of the program"
		
	dbc.close()