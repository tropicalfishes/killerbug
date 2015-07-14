# -*- coding: GBK -*-

def GetScriptPath():
	import os, sys
	print sys.path[0]
	print os.path.realpath(__file__)
	print os.path.split(os.path.realpath(__file__))
	return os.path.split(os.path.realpath(__file__))[0]
