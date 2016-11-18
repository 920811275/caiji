#!D:/Python/python.exe
# -*- coding: UTF-8 -*-
#print "Content-type:textml"

import MySQLdb
import re
import ConfigParser
config = ConfigParser.ConfigParser()
# print dbhost,dbport,dbname,dbuser,dbpassword,dbcharset
# 

class MysqldbHelper:
 
	def __init__(self):
			config.read('db.conf')
			dbhost = config.get("database", "dbhost")
			dbport = config.get("database", "dbport")
			dbname = config.get("database", "dbname")
			dbuser = config.get("database", "dbuser")
			dbpassword = config.get("database", "dbpassword")
			dbcharset = config.get("database", "dbcharset")
			conn=MySQLdb.connect(dbhost,dbuser,dbpassword,dbname,charset="UTF8")
			self.cursor = conn.cursor()
	#采集过滤div ''
	def getguo(self,x):
		pattern = re.compile('<div .*?</div>',re.S)
		res = re.sub(pattern,'',x)
		return res

	#单个删除
	def getdel(self,table,id):
			cursor = self.cursor
			try:
				sql="DELETE FROM "+table+" WHERE id="+id
				cursor.execute(sql)
				return 'true'
			except MySQLdb.Error as e:  
				print ( "getdel Error %d: %s" % (e.args[0],e.args[1]) )
	#查询表中所有数据
	def getselect(self,table):
			cursor = self.cursor
			try:
				sql="SELECT * FROM "+table
				cursor.execute(sql)
				result = cursor.fetchall()
				return result
			except MySQLdb.Error as e:  
				print ( "getdel Error %d: %s" % (e.args[0],e.args[1]) )
	#批量删除
	def getdell(self,table,id):
			cursor = self.cursor
			try:
				sql="DELETE FROM "+table+" WHERE id in ("+id+")"
				cursor.execute(sql)
				return 'true'
			except MySQLdb.Error as e:  
				print ( "getdel Error %d: %s" % (e.args[0],e.args[1]) )	 	
	#修改
	def getupdate(self,table,data,id):
			cursor = self.cursor
			try:
				sql="UPDATE "+table+" SET "+data+" WHERE id = "+id
				cursor.execute(sql)
				return 'true'
			except MySQLdb.Error as e:  
				print ( "getdel Error %d: %s" % (e.args[0],e.args[1]) )

	#添加导航
	def getadd(self,new):
			res = MysqldbHelper()
			cursor = self.cursor
			add = new
			for i in add:
				print i[0],res.getguo(i[1])
				val = res.getguo(i[1])
				sql = """INSERT INTO KAO(uname,pwd)VALUES (%s, %s)""" %("'"+val.decode('GB2312','ignore').encode('utf8')+"'","'"+i[0]+"'")	
				cursor.execute(sql)
	
	#添加标题 和 链接
	def gettitle(self,new):
			res = MysqldbHelper()
			cursor = self.cursor
			add = new
			for i in add:
				print i[0],res.getguo(i[1])
				val = res.getguo(i[1])
				sql = """INSERT INTO title(title,url)VALUES (%s, %s)""" %("'"+val.decode('GB2312','ignore').encode('utf8')+"'","'"+i[0]+"'")	
				cursor.execute(sql)