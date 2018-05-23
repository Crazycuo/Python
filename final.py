#/usr/bin/python 
# encoding:utf-8
# __Author__ = Slwhy

import requests
import time
import random
import hashlib
import json

#i = "" + ((new Date).getTime() + parseInt(10 * Math.random(), 10))
i = str(int(time.time()*1000)+random.randint(1,10))
#o = n.md5("fanyideskweb" + t + i + "aNPG!!u6sesA>hBAW1@(-");
t = input("please input the word you want to translate:")
u = 'fanyideskweb'
l = 'aNPG!!u6sesA>hBAW1@(-'
src = u + t + i + l# u 与 l 是固定字符串，t是你要翻译的字符串，i是之前的时间戳
m2 = hashlib.md5()
m2.update(src.encode("utf8"))
str_sent = m2.hexdigest()

''' 
    i:number
    from:AUTO
    to:AUTO
    smartresult:dict
    client:fanyideskweb
    salt:1515462554510
    sign:32ea4a33c063d174a069959a5df1a115
    doctype:json
    version:2.1
    keyfrom:fanyi.web
    action:FY_BY_REALTIME
    typoResult:false
'''
head = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,zh-TW;q=0.7',
    'Connection': 'keep-alive',
    'Content-Length': '16',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'Host': 'fanyi.so.com',
    'Origin': 'http://fanyi.so.com',
    'Referer': 'http://fanyi.so.com/',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/66.0.3359.139 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest',
}
head['Cookie'] = '__guid=144965027.3785044701417153500.1526999310786.1252; count=1'
# '___rl__test__cookies=1515471316884'

data = {
'query':t,
'eng':'1',
}

s = requests.session()
#url = 'https://dsuggest.ydstatic.com/suggest.s?query=hello&keyfrom=dict2.top.suggest&o=form&rn=10&h=22&le=eng'
url = 'http://fanyi.so.com/index/search'
p = s.post(url,data= data,headers = head)

myjson=json.loads(p.text)
print (myjson['data']['explain']['phonetic']['英'])
print (myjson['data']['explain']['phonetic']['美'])
#print (json.dumps(myjson,ensure_ascii=False)['data'])
#print (repr(p.text))
