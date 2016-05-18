#!/usr/bin/env python

import time

def GetNowTime():
	return time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))

def main():
	now_time = GetNowTime()
	docname = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
	docname = '/home/gallop/data/' + docname + '.txt'
	print now_time, '\n', docname
	f = open(docname,'w')
	try:
		f.write('ok\n')
		print 'The file is opened '
	finally:
		f.close()
		print 'The file is closed'
	d = [[(1,2,3),(2,3,4),(5,6,7)],[(1,2,3),(2,3,4),(5,6,7)],[(1,2,3),(2,3,4),(5,6,7)]]
	s = ''
	for i in  d :
		for j in i :
			s += '%d	%d	%d	' %j
		s +='\n'
	f = open(docname, 'a')
	try:
		print 'The file is opened '
		f.write(s)

		
	finally:
		f.close()
		print 'The file is closed'






if __name__ == '__main__':
	main()