# -*- coding: GBK -*-
import httplib
import time

g_ConnectionList = []

def	RequestData(addr, port=None, cb=None):
	import save, misc
	conn = httplib.HTTPConnection(addr, port)
	print "����ʼʱ��", time.time()
	conn.request("GET", '/')
	print "�������ʱ��", time.time()
	response = conn.getresponse()
	print "�õ�response", time.time()
	status = response.status
	reason = response.reason
	body = response.read()
	print "�õ�response����", time.time()
	print status, reason, len(body)
	scriptPath = misc.GetScriptPath()
	print "��ǰ�ű�·��", scriptPath
	filePath = scriptPath + "/dingbady.html"
	save.WriteToFile(body, filePath)


