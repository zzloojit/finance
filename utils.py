import csv
import os
import sys

def csv2list(filename):
	l = list()
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			l.append(row)
	return l

def is3vplus(l):
	test = 3
	p = 0
	for i in range (1, len(l) - 1):
		if test == 0:
			break
		v = int(l[i][5])
		if v == 0:
			continue

		if p == 0:
			p = v
		else:
			if p - v < 0:
				return False
			p = v
		test -=1
	if test == 0:
		return True
	return False

def isgreed(l):
	for i in range (0, len(l)):
		if int(l[i][5]) == 0:
			continue

		if float(l[i][4]) >= float(l[i][1]):
			return False
		return True
	return False

def is3red(l):
	if len(l) < 3:
		return False
	test = 3
	for i in range(0, len(l) -1):
		if test == 0:
			break
		if int(l[i][5]) == 0:
			continue
		if (float(l[i][4]) <= float(l[i][1])):
			break
		if (float(l[i][4]) <= float(l[i+1][4])):
			break
		test -= 1
	if test == 0:
		return True
	return False

def check3red(l):
	pass

if __name__ == '__main__':
	total = 0
	if len(sys.argv) != 2:
		print "follow csv dir"
	if os.path.isdir(sys.argv[1]) != True:
		print "need a dir"

	os.chdir(sys.argv[1])
	files = os.listdir(sys.argv[1])
	for f in files:
		if f.endswith(".csv"):
			l = csv2list(f)
			if is3red(l[1:]) and is3vplus(l[1:]):
				print f
			 	total += 1
	print "total :" , total
	#l = csv2list("yahoo201547/000026.sz.csv")
	#print is3red(l[1:])