# -*- coding: GBK -*-
import urllib2
import threading

g_ThreadingPool = [] #ҵ�����̵߳�����

def GetDataFromUrl(addr, port, cb, args):
	try:
		respone = urllib2.urlopen(addr)	#urllib2.urlopen()��read()�����ӿڶ��������͵�
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
