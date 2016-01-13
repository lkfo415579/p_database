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
	print(">>> new ranking_all(mode='%s', page=1, per_page=%d , date=%s)" % (mode,per_page,date),file=r_f)
	print(">>> new ranking_all(mode='%s', page=1, per_page=%d , date=%s)" % (mode,per_page,date))
	#rank_list = api.sapi.ranking("all", 'day', 1)
	#rank_list = api.papi.ranking_all('daily', 1, 50)
	rank_list = api.papi.ranking_all(mode, 1, per_page, date=date)
	#print rank_list

	# more fields about response: https://github.com/upbit/pixivpy/wiki/sniffer
	ranking = rank_list.response[0]
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
	print (ranking)
	
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
		tool.database_insertation(work,info_log)
		################
		##retrieve image data
		#sys.exit()
		image_data = api.papi.get_image(ori_url)
		#print image_data
		with open("%s/%s_%s.%s" % (path,rank,id,type), 'wb') as out_file:
			shutil.copyfileobj(image_data, out_file)
		#f = open("%s%s.jpg" % (path,id), 'wb')
		#f.write(image_data)
		#f.close()
		if index > per_page-1:
			break
	#print ">>> origin url: %s" % illust.image_urls['large']


def main():
	api = PixivAPI()

	### change _USERNAME,_PASSWORD first!
	api.login(_USERNAME, _PASSWORD)
	###
	year = '2015'
	mode = 'daily'
	global prepath
	prepath = '2015_daily'
	import os
	if not os.path.exists(prepath):
		os.makedirs(prepath)
	print ('FOLDER PATH : %s' % prepath)
	print ('FOLDER PATH : %s' % prepath,file=r_f)
	for month in range(1,13):
		####

		#mode = 'weekly'
		per_page = 10
		for day in range(1,32):
			date = '%s-%02d-%02d' % (year,month,day)
			id_list = []
			id_list = migrate_sapi_to_papi(api,mode,per_page,date)
			#for database
			#page = 1
			global info_log
			info_log ={'page':1,'mode':mode,'per_page':per_page,'date':date}
			#
			fetch_image(api,id_list,per_page)

if __name__ == '__main__':
	main()
