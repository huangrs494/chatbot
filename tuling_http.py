# -*- coding: utf-8 -*-
import urllib,urllib2
import sys
import json

reload(sys)
sys.setdefaultencoding('utf-8')

API_KEY = 'e22e606e36f3403a9f2887b417653029'
raw_TULINURL = "http://www.tuling123.com/openapi/api?key=%s&info=" % API_KEY

def result():
    #for i in range(1, 50):
    #print "我:".decode('utf-8')
    queryStr =  raw_input("我：".decode('utf-8'))
    TULINURL = "%s%s" % (raw_TULINURL,urllib2.quote(queryStr))
    req = urllib2.Request(url=TULINURL)
    result = urllib2.urlopen(req).read()
    hjson=json.loads(result)
    length=len(hjson.keys())
    content=hjson['text']

    if length==3:
        return 'robots:' +content+hjson['url']
    elif length==2:
        return 'robots:' +content

if __name__=='__main__':
    print "你好，请输入内容:".decode('utf-8')
    for i in range(1,50):
        contents=result()
        print contents