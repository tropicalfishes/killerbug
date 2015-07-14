#using utf_8
import httplib
import time

g_ConnectionList = []

def	RequestData(addr, port=None, cb):
	conn = httplib.HTTPConnection(addr, port)
	print "请求开始时间", time.time()
	conn.request("GET", '/')
	print "请求结束时间"


