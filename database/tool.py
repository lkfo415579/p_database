global sys_log
sys_log = True

def sys_log_OT(db,dbc):
	global sys_log
	if sys_log:
		sys_log = False
		from database import config
		import datetime
		sys_sql = "insert into sys_log (start_date,username) values('%s','%s');" % (str(datetime.datetime.now()),config._USERNAME)
		print (sys_sql)
		dbc.execute(sys_sql)
		db.commit()

def Main_database_insert(insert_dict,info_log,user,stats):
	import MySQLdb
	
	db = MySQLdb.connect(host='127.0.0.1', user='lkfo', passwd='qq321520', db='pixiv')
	db.set_character_set('utf8')
	dbc= db.cursor()
	dbc.execute('SET NAMES utf8;')
	dbc.execute('SET CHARACTER SET utf8;')
	dbc.execute('SET character_set_connection=utf8;')
	#insert_dict = {'drink':'horchata', 'price':10}

	#log writting
	try:
		###write_sys_log only first time##
		sys_log_OT(db,dbc)
		##############
		###insert_info_log
		sql_infolog = sql_insertFromDict("info_log", info_log)
		dbc.execute(sql_infolog, info_log)
		db.commit()
	except MySQLdb.Error, e:
		try:
			if e.args[0] != 1062:
				print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
		except IndexError:
			print "MySQL Error: %s" % str(e)
	#real data writting
	try:
		#dbc.execute()
		###insert pictures
		sql_pic = sql_insertFromDict("pictures", insert_dict)
		##insert user
		sql_user = sql_insertFromDict("user", user)
		##insert stats
		sql_stats = sql_insertFromDict("stats", stats)
		#print ("SQL")
		#print (sql)
		dbc.execute(sql_pic, insert_dict)
		db.commit()
		dbc.execute(sql_user, user)
		db.commit()
		dbc.execute(sql_stats, stats)
		db.commit()
		print ("Updated Database!")
	except MySQLdb.Error, e:
		try:
			if e.args[0] != 1062:
				print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
			else:
				print "@Has already exited data"
			#print "MySQL Error [%d]: %s" % (e.args[0], e.args[1])
			
		except IndexError:
			print "MySQL Error: %s" % str(e)
		#print (db.rollback())
	#db.close()

def sql_insertFromDict(table, myDict):
	"""Take dictionary object dict and produce sql for 
	inserting it into the named table"""
	#
	#values = convert_dic(myDict)
	sql = 'INSERT INTO ' + table
	sql += ' ('
	sql += ', '.join(myDict)
	sql += ') VALUES ('
	#sql += ', '.join(map(dictValuePad, myDict))
	#print (map(dictValuePad, myDict))
	sql += ', '.join(convert_dic(myDict))
	sql += ');'
	#
	'''placeholders = ', '.join(['%s'] * len(myDict))
	columns = ', '.join(myDict.keys())
	sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)'''
	return sql
	
def convert_dic(myDict):
	list = []
	for key,value in myDict.iteritems():
		#print (type(value))
		if isinstance(value,int):
			list.append('%(' + str(key) + ')s')
		else:
			list.append('%(' + str(key) + ')s')
		#list.append('%(' + str(key) + ')s')
	return list
	
def dictValuePad(key):
	#print (value)
	return '%(' + str(key) + ')s'
	
def process_tags(tags):
	tmp_string = "["
	for tag in tags:
		tmp_string = tmp_string + '"'+tag.decode('utf8')+'"' +','
	tmp_string = tmp_string[:-1] + ']'
	return tmp_string
	
def database_insertation(work,info_log):
	#print ("Updated Database!")
	#delete all unnecessary data
	items = ["image_urls","user","stats"]
	image_urls = work["image_urls"]
	#
	user = work["user"]
	user['user_id'] = user['id']
	user['id'] = work['id']
	##
	stats = work["stats"]
	stats['id'] = work['id']
	stats['date'] = info_log['date']
	#print (work)
	for item in items:
		del work[item]
	###
	##process tags##
	work['tags'] = process_tags(work['tags'])
	##END@@process tags##
	##
	
	Main_database_insert(work,info_log,user,stats)
	