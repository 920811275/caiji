#!d:/python/python.exe
# -*- coding: UTF-8 -*-
print
from conf import *
import urllib
import urllib2
import MySQLdb
import re
res = MysqldbHelper()

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

	def getTitle(self):
		page = self.geturl()
		pattern = re.compile('(<div id="pane-news" .*?)<div id="footerwrapper">',re.S)
		tit = re.search(pattern,page)
		patterncode = re.sub(r'<a .*?><img .*?</a>','',tit.group(1))
		patterncode = re.sub(r'<a .*?>\n<img .*?\n</a>','',patterncode)
		return patterncode


	def getHref(self):
		hrefcode = self.getTitle()
		pattern = re.compile('<a href="(http://.*?)".*?>(.*?)</a>', re.S)
		itmes = re.findall(pattern, hrefcode)
		return itmes

newi = News()
new = newi.getHref()
# print new
res = res.gettitle(new)
