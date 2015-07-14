# -*- coding: GBK -*-
import httplib
import time

g_ConnectionList = []

def	RequestData(addr, port=None, cb=None):
	import save, misc
	conn = httplib.HTTPConnection(addr, port)
	print "请求开始时间", time.time()
	conn.request("GET", '/')
	print "请求结束时间", time.time()
	response = conn.getresponse()
	print "得到response", time.time()
	status = response.status
	reason = response.reason
	body = response.read()
	print "得到response数据", time.time()
	print status, reason, len(body)
	scriptPath = misc.GetScriptPath()
	print "当前脚本路径", scriptPath
	filePath = scriptPath + "/dingbady.html"
	save.WriteToFile(body, filePath)


