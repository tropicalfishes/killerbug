# -*- coding: GBK -*-
import threading

LOCKTIMEOUT = 120
TESTURL = ["http://www.baidu.com", "http://hao.360.cn/", "https://www.taobao.com/", "http://www.163.com/", "http://finance.ifeng.com/", "http://www.aol.com/"]

g_ThreadingLock = threading.Lock()

def OnLoadFinish(bSucsess, data, id, url):
	import time
	if g_ThreadingLock.acquire(LOCKTIMEOUT):
		print id, url, time.time(), len(data)
		g_ThreadingLock.release()
	else:
		import misc
		misc.PrintError("ERROR:获取锁超时")

def Main():
	import net, random, misc
	for i in xrange(10):
		cnt = len(TESTURL)
		iRand = random.randint(0, cnt-1)
		net.RequestData(TESTURL[iRand], None, OnLoadFinish, i, TESTURL[iRand])
	misc.PrintError("试一下")

Main()