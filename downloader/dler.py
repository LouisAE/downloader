import sys
import requests
from time import sleep
import re
import os
import argparse

#custom error
class dlError(Exception):
    def __init__(self,error):
        self.error = error
    def __str__(self,*args,**kwargs):
        return self.error

#basic classes
class Menu():
    pass

#constant variable area
addr = "D:/开发/C++/testfile/"

def get_args():
    parser = argparse.ArgumentParser(description = \
        "Download file(s) from appointed URLs")
    parser.add_argument("-u","--url",action = 'store',dest="urls",type=str,\
        help="The url which should contain the protol name.\n \
        For example, \"https://example.com/\" is right while \"example.com\" is wrong.")
    parser.add_argument("-o","--output",action = 'store',dest="filename",type=str,help=\
        "The location of output file(s)")
    return parser.parse_args(sys.argv[1:])




def download(url,file,mode):
    """
    获取文本或二进制数据
    mode参数可以是：text,binary。
    默认为text,默认文件名为temp.txt
    """
    try:
        h = {}
        h["User-Agent"] = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko)\
        Chrome/89.0.4389.82 Safari/537.36 Edg/89.0.774.50"
        u = requests.get(url,headers=h).content

        if mode == "text":
            r = u.decode("utf-8")
            with open(file,"w",encoding="utf-8") as f:
                f.write(r)
            print("SUCCESS:"+file)

        elif mode == "binary":
            r = u
            with open(file,"wb") as f:
                f.write(r)
            print("SUCCESS:"+file)
        else:
            raise argError("No such mode:"+mode)

    except Exception as e:
        print("ERROR:",end = '\0')
        print("文件\""+url+"\"下载失败")
        print(e)
        print("Skipping...")
        #os.system("pause")

def dl_multiply(s = 0,e = float("inf")):
    f2 = open(addr+"temp.txt","r",encoding="utf-8")
    f2c = f2.read()
    f2.close()
    title = re.search("(?<=<h1\>).+(?=</h1\>)",f2c).group()
    if not os.path.exists(addr+title):
        os.mkdir(addr+title)
    pic_url = re.findall("<img class=\"vimg\" src=\"(.+)\"\><",f2c)

    i = 0
    for u in pic_url:
        i+=1
        if(i<s):
            continue
        if(i>e):
            break
        download(u,addr+title+"/"+str(i)+u[-4:],"binary")
        sleep(1)




def main():
    url = input("Input URL:")
    download(url,addr+"temp.txt","text")
    #args=get_args()
    #print(args)
    #download(args.urls,args.filename,"binary")
if __name__ == "__main__":
    main()




#.8.29.2021日志：使用retry时若被装饰函数中有错误处理语句，则
#错误会被吞掉，不会触发retry
