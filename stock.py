# -*- coding: GBK -*-

KEYS = ["name", "todayopenprice", "yesterdayendprice", "curprice", "todaymaxprice", "todayminprice", "buy1",
"sell1","dealnum", "dealmoneycnt", "buy1num", "buy1price", "buy2num", "buy2price", "buy3num", "buy3price",
"buy4num", "buy4price", "buy5num", "buy5price", "sell1num", "sell1price", "sell2num", "sell2price", 
"sell3num", "sell3price", "sell4num", "sell4price", "sell5num", "sell5price", "day", "time",]


def GetSearchCode(id):
	code = str(id)
	if len(code) != 6:
		return
	if code.startswith("300") or code.startswith("000") or code.startswith("002"):
		return "sz"+code
	elif code.startswith("600") or code.startswith("601"):
		return "sz"+code

def ParsingData(s):
	import misc
	begin = s.find('"')+1
	end = s.rfind('"')
	if begin == -1 or end == -1 or begin >= end:
		misc.PrintError("ERROR:得到数据格式不对:%s"%s)
		return 
	s = s[begin, end]
	lData = s.split(",")
	dData = misc.List2Dict(KEYS, lData)
	return dData
	

