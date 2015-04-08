import csv
import os

def csv2list(filename):
	l = list()
	with open(filename, 'rb') as f:
		reader = csv.reader(f)
		for row in reader:
			l.append(row)
	return l

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
	l = csv2list("yahoo201547/000026.sz.csv")
	print is3red(l[1:])