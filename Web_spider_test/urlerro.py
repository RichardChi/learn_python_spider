import urllib2

requset = urllib2.Request('http://blog.csdn.net/cqcre')
try:
    urllib2.urlopen(requset)
except urllib2.HTTPError, e:
    print e.code
except urllib2.URLError, e:
    print e.reason
else:
    print "OK"



