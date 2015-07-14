# -*- coding: GBK -*-

def WriteToFile(s, path):
	f = file(path, "w")
	try:
		f.write(s)
	except:
		print "---->>>>Script Error: write file failed"
	finally:
		f.close()
	