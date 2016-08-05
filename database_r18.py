#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import print_function
r_f = open('log','w')
import datetime
print ('Start Date:%s' % datetime.datetime.now(),file=r_f)
print ('Start Date:%s' % datetime.datetime.now())
###
import sys 
reload(sys) 
sys.setdefaultencoding('utf8')

from pixivpy2 import *

from database import tool

from database import config

_USERNAME = config._USERNAME
_PASSWORD = config._PASSWORD


# def sapi_demo(api):
# 	print(">>> ranking(male, day, page=1)")
# 	rank_list = api.sapi.ranking("all", 'day', 1)
# 	for img in rank_list:
# 		print(img)

# 	illust = api.sapi.get_illust(46363414)
# 	print(">>> [%s] %s: %s" % (illust.authorName, illust.title, illust.url))

# 	print(">>> get_user(id=1184799, level=3)")
# 	user = api.sapi.get_user(1184799, level=3)
# 	print("%s: %s" % (user.author_name, user.thumbURL))

# 	## Authentication required! call api.login first!
# 	print(">>> sapi.get_bookmark(1418182, page=1)")
# 	bookmark_list = api.sapi.get_bookmark(1418182)
# 	for img in bookmark_list:
# 		print(img)

#prepath = 'H_'
def migrate_sapi_to_papi(api,mode,per_page,date):
	#daily,weekly,monthly
	#mode=male&date=20150704
	#mode = 'male'
	###############
	#mode = 'weekly_r18'
	#per_page = 30
	#date = '2015-06-12'
	page = int(per_page/10)
	
	print(">>> new ranking_all(mode='%s', page=%d, per_page=%d , date=%s)" % (mode,page,per_page,date),file=r_f)
	print(">>> new ranking_all(mode='%s', page=%d, per_page=%d , date=%s)" % (mode,page,per_page,date))
	#rank_list = api.sapi.ranking("all", 'day', 1)
	#rank_list = api.papi.ranking_all('daily', 1, 50)
	##first one
	rank_list = api.papi.ranking_all(mode,1, per_page, date=date)
	
	tmp_rank_list = []
	for x_page in range(2,page+1):
		try:
			tmp_rank_list.append(api.papi.ranking_all(mode,x_page, per_page, date=date).response[0])
		except:
			pass
	

	# more fields about response: https://github.com/upbit/pixivpy/wiki/sniffer
	try:
		ranking = rank_list.response[0]
		#print (ranking)
		for node in tmp_rank_list:
			ranking['works'] = ranking['works'] +node['works']
		###combine all pages info together####
	except:
		ranking = None
	#print ranking
	#for img in ranking.works:
		#print img.work
		#print "[%s/%s(id=%s)] %s" % (img.work.user.name, img.work.title, img.work.id, img.work.image_urls.px_480mw)
	
	return ranking
def papi_demo(api):
	json_result = api.papi.works(46363414)
	#print json_result
	illust = json_result.response[0]
	print (">>> origin url: %s" % illust.image_urls['large'] , file=r_f)

	#json_result = api.papi.users(1184799)
	#print json_result
	#user = json_result.response[0]
	#print user.profile.introduction

	
def fetch_image(api,ranking,per_page):
	import shutil
	
	#path = prepath+'images'
	path = prepath
	#print type(id_list)
	#print ">>> origin url: %s" % node.image_urls['large']
	#illust = id_list[0]
	###BIG DISPLAY###
	#print (ranking)
	
	index = 0
	for img in ranking.works:
		index += 1
		id =  img.work.id
		print (img.work.image_urls.large,file=r_f)
		ori_url = img.work.image_urls.large
		print ('Title : %s' % img.work.title,file=r_f)
		print ('Title : %s' % img.work.title)
		#
		type = ori_url[-3:]
		#print type
		##
		rank = img.rank
		print ('Rank : %s' % rank ,file=r_f)
		print ('Rank : %s' % rank )
		##before saving image data###
		#########
		#database
		#use work to insert data
		work = img.work
		work['rank'] = img.rank
		work['previous_rank'] = img.previous_rank
		#
		user = work['user']
		#
		################
		##retrieve image data
		#sys.exit()
		image_data = api.papi.get_image(ori_url)
		#picture_name
		u_name = str(user.name.decode('utf8'))
		p_name = str(img.work.title.decode('utf8'))
		pic_name = str(u_name+'-'+p_name+'('+str(id)+')')
		#pic_name = ''.join(e for e in pic_name if e != "//" or e != "\\")
		pic_name = pic_name.replace("/","")
		pic_name = pic_name.replace("\\","")
		print ("Picture name : %s" % pic_name)
		###
		pic_path = "%s/%s.%s" % (path,pic_name,type)
		import os.path
		if not os.path.isfile(pic_path):
			with open(pic_path, 'wb') as out_file:
				shutil.copyfileobj(image_data, out_file)
		#f = open("%s%s.jpg" % (path,id), 'wb')
		#f.write(image_data)
		#f.close()
		##########end , write into database###
		work['image_files_name'] = pic_path
		tool.database_insertation(work,info_log)
		
		if index > per_page-1:
			break
	#print ">>> origin url: %s" % illust.image_urls['large']


	
	
def main(year=2015,month_set=1,per_page=20):
	api = PixivAPI()

	### change _USERNAME,_PASSWORD first!
	api.login(_USERNAME, _PASSWORD)
	###
	#year = '2015'
	mode = 'daily_r18'
	global prepath
	prepath = str(year) + '_daily_r18'
	import os
	if not os.path.exists(prepath):
		os.makedirs(prepath)
	print ('FOLDER PATH : %s' % prepath)
	print ('FOLDER PATH : %s' % prepath,file=r_f)
	for month in range(month_set,13):
		####

		#mode = 'weekly'
		#per_page = 20
		for day in range(1,32):
			date = '%s-%02d-%02d' % (year,month,day)
			id_list = []
			id_list = migrate_sapi_to_papi(api,mode,per_page,date)
			
			#check whether it is sucess or not
			if id_list == None:
				#didn't get a single response from pixiv
				continue
			
			print ("Total images of this day : %d" % len(id_list['works']))
			#for database
			#page = 1
			global info_log
			info_log ={'page':int(per_page/10),'mode':mode,'per_page':per_page,'date':date}
			#
			fetch_image(api,id_list,per_page)

if __name__ == '__main__':
	try:
		if sys.argv[1] == '-h':
			print ("Usage:python database.py [year=2015] [month=1] [per_page=20]")
			print ("Description: Haha")
			#print "data_folder : the target folder which the program is going to scan."
			sys.exit()
	except:
		pass
		
	if len(sys.argv) > 1:
		year = sys.argv[1]
	else:
		year = 2015
	if len(sys.argv) > 2:
		month = int(sys.argv[2])
	else:
		month = 1
	if len(sys.argv) > 3:
		per_page = sys.argv[3]
	else:
		per_page = 20
		
		
	main(year,month,per_page)
