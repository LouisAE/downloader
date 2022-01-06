import dler
import re
import urllib.request as ur

def withdraw():
    f = open(dler.addr+"addr.txt","r",encoding="utf-8")#addr.txt需手动获取
    s = f.read()
    f.close()
    r = re.findall("(?<=<a target=\"main\" class=\"jump\" href=\").+(?=\">)",s)
    url = "https://hydrozoa.felisworks.com/doc/tjs2doc/contents/"
    for i in r:
        dler.get_info(url+i,dler.addr+i)


def main():
    withdraw()
        
    
    

#main()

#以下为下载多个网页中图片的代码，用于kr2doc
#已经改为多个网页

"""
f = open(dler.addr+"1.txt","r",encoding="utf-8")
for i in f.readlines():
    h = {}
    h["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
    Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
    u = ur.Request("https://hydrozoa.felisworks.com/doc/kr2doc/contents/"+i,headers=h)
    u = ur.urlopen(u)
    r = u.read().decode("shift-jis")
    fin = re.findall("(?<=<a class=\"jump\" href=\").+(?=\">)",r)
    for each in fin:
        dler.get_info("https://hydrozoa.felisworks.com/doc/kr2doc/contents/"+each,dler.addr+each)
"""
