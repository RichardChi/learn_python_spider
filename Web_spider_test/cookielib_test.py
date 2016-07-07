import urllib2
import cookielib

cookie = cookielib.CookieJar()
filename = 'cookie.txt'
cookiet = cookielib.MozillaCookieJar(filename)

handler = urllib2.HTTPCookieProcessor(cookie)
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
for item in cookie:
    print 'Name=' + item.name
    print 'Value=' + item.value


handler = urllib2.HTTPCookieProcessor(cookiet)
opener = urllib2.build_opener(handler)

response = opener.open('http://www.baidu.com')
cookiet.save(ignore_discard=True,ignore_expires=True)



