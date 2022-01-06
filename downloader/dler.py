import urllib.parse
import urllib.request as ur
import urllib.error as ue
from time import sleep
import requests
import re
import os
from retrying import retry

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

#@retry(stop_max_attempt_number=3)
def get_info(url,file = addr + "temp.txt",mode = "text"):
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

def main():
    get_info("https://i1.lspcdn.xyz/galleries/2040509/203.jpg",addr+"203.jpg","binary")
    os.system("pause")

if __name__ == "__main__":
    main()




#.8.29.2021日志：使用retry时若被装饰函数中有错误处理语句，则
#错误会被吞掉，不会触发retry
