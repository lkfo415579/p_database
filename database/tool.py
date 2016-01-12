def insertFromDict(table, dict):
	import MySQLdb
	db = MySQLdb.connect(host='127.0.0.1', user='lkfo', passwd='qq321520', db='pixiv')
	db.set_character_set('utf8')
	dbc= db.cursor()
	dbc.execute('SET NAMES utf8;')
	dbc.execute('SET CHARACTER SET utf8;')
	dbc.execute('SET character_set_connection=utf8;')
	#insert_dict = {'drink':'horchata', 'price':10}
	insert_dict = dict
	sql = sql_insertFromDict(table, insert_dict)
	print ("SQL")
	print (sql)
	try:
		#dbc.execute(sql, insert_dict.values())
		dbc.execute(sql, insert_dict)
		db.commit()
	except:
		print (db.rollback())
	db.close()

def sql_insertFromDict(table, myDict):
	"""Take dictionary object dict and produce sql for 
	inserting it into the named table"""
	#
	values = convert_dic(myDict)
	sql = 'INSERT INTO ' + table
	sql += ' ('
	sql += ', '.join(myDict)
	sql += ') VALUES ('
	sql += ', '.join(map(dictValuePad, myDict))
	sql += ');'
	#
	'''placeholders = ', '.join(['%s'] * len(myDict))
	columns = ', '.join(myDict.keys())
	sql = "INSERT INTO %s ( %s ) VALUES ( %s )" % (table, columns, placeholders)'''
	return sql
	
def convert_dic(myDict):
	list = []
	for (key,value) in myDict:
		if type(value) == 'int':
			list.append('%(' + str(key) + ')i')
		else:
			list.append('%(' + str(key) + ')s')
	
def dictValuePad(key,value):
	print (value)
	return '%(' + str(key) + ')s'

	
def database_insertation(work):
	print ("hey there")
	items = ["image_urls","user","tags","stats"]
	for item in items:
		image_urls = work[item]
		del work[item]
	
	insertFromDict("pictures",work)
	