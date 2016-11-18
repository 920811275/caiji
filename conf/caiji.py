#!D:/Python/python.exe
# -*- coding: UTF8 -*-
print
import urllib
import urllib2
import MySQLdb
import re

class News:
	def __init__(self):
		self.url = "http://news.baidu.com/"

	def getguo(self,x):
		pattern = re.compile('<div .*?</div>',re.S)
		res = re.sub(pattern,'',x)
		return res

	def geturl(self):
		url = self.url
		request = urllib2.Request(url)
		response = urllib2.urlopen(request)
		return response.read()

	def getnav(self):
		nav = self.geturl()
		pattern = re.compile('(<div id="channel-all" class="channel-all clearfix".*?)<i class="slogan"></i>', re.S)
		navCode = re.search(pattern, nav)
		return navCode.group(1)

	def getnavs(self):
		navs = self.getnav()
		pattern = re.compile('<a href="(http://.*?)/.*?>(.*?)</a>', re.S)
		navCode = re.findall(pattern,navs)
		return navCode
		
db = MySQLdb.connect("127.0.0.1","root","123","php10",charset="gbk")
cursor = db.cursor()
newi = News()
new = newi.getnavs()
for i in new:
	print i[0],newi.getguo(i[1])
	val = newi.getguo(i[1])
	sql = """INSERT INTO KAO(uname,pwd)VALUES (%s, %s)""" %("'"+val+"'","'"+i[0]+"'")
	#vala = (vall,val[0])
	try:
		# 执行sql语句
		cursor.execute(sql)
		# 提交到数据库执行
		db.commit()
	except:
		# Rollback in case there is any error
		db.rollback()