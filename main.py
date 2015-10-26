# -*- coding: GBK -*-
import threading

LOCKTIMEOUT = 120
TESTURL = ["http://www.baidu.com", "http://hao.360.cn/", "https://www.taobao.com/", "http://www.163.com/", "http://finance.ifeng.com/", "http://www.aol.com/"]

g_ThreadingLock = threading.Lock()

def OnLoadFinish(bSucsess, data):
	import time, misc, stock
	if g_ThreadingLock.acquire(LOCKTIMEOUT):
		dData = stock.ParsingData(data)
		for sKey, v in dData.iteritems():
			print sKey, ":", v
		g_ThreadingLock.release()
	else:
		import misc
		misc.PrintError("ERROR:获取锁超时")

def Main():
	import net, stock
	stockId = "002153"
	sCode = stock.GetSearchCode(stockId)
	url = "http://hq.sinajs.cn/list=%s"%sCode
	print "url", url
	net.RequestData(url, None, OnLoadFinish)

Main()