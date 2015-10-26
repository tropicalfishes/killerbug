# -*- coding: GBK -*-
import urllib2
import urllib
import threading

g_ThreadingPool = [] #业务层对线程的引用

def GetDataFromUrl(addr, port, cb, args):
	try:
		value = {'name':'Michael Foord', 'location':'Northampton', 'language':'Python' }
		data = urllib.urlencode(value)
		headers = {'User-Agent':'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'}
		req = urllib2.Request(addr, data, headers)
		respone = urllib2.urlopen(req)	#urllib2.urlopen()和read()两个接口都是阻塞型的
		body = respone.read()
		respone.close()
		if cb:
			cb(True, body, *args)
	except:
		if cb:
			cb(False, 0, *args)

def	RequestData(addr, port, cb, *args):
	th = threading.Thread(target=GetDataFromUrl, args=(addr, port, cb, args))
	th.start()	
