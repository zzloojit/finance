import csv
import urllib2
import httplib
import Queue
import threading
import time

work_queue = Queue.Queue(15000)
lock = threading.Lock()

def getCSV():
	while work_queue.empty() != True:
		code = work_queue.get()
		print work_queue.qsize()
		url = "http://ichart.finance.yahoo.com/table.csv?s=" + code
		try:
			response = urllib2.urlopen(url, timeout = 10)
			if response.getcode() == 200:
				f = open("yahoo201547/" + code + ".csv", "wb")
				f.write(response.read())
				f.close()
		# except urllib2.HTTPError, e:
		# 	print e.code, e.reason
		# 	if e.code != 404:
		# 		work_queue.put(code)
		except urllib2.URLError, e:
			lock.acquire()
			print e.code, e.reason
			f = open("yahoo.getcsv.log", "a")
			f.write("\n" + code + ":")
			f.write(e.reason)
			f.close()
			lock.release()
		except Exception, e:
			print e
			work_queue.put(code)

def getCSV2(code):
	url = "http://table.finance.yahoo.com"
	param = "/table.csv?s=" + code
	conn = httplib.HTTPConnection(url, 80, timeout=10)
	conn.request("GET", "/index.html")
	response = conn.getresponse()
	print response.status, response.reason

#getCSV("600001.ss
def pushList():
	for i in range(600000, 604000):
		work_queue.put("%s.ss" % i)
		#getCSV("%s.ss" % i)
		pass
	for i in range(1000000, 1004000):
	 	k = ("%s.sz" % i)[1:]
	# 	print k
		work_queue.put(k)

	for i in range(300000, 304000):
		work_queue.put("%s.sz" % i)

def getList():
	for i in range (100):
		t = threading.Thread(target = getCSV)
		t.setDaemon(True)
		t.start()

if __name__ == '__main__':
	pushList()
	getList()
	getCSV()
	
