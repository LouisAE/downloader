from dler import *
"""
2021.9.9笔记
当包含一个模块时，模块中已经包含的模块不会被一同包含
但如果使用 from module import * 的话却可以
如dler中已经包含re，若使用import dler，此文件中含re的语句将出错
除非改为dler.re
但用from dler import * 就没有问题
"""

def withdraw_address(s = 0,e = float("inf")):#提取图片网址并下载
    f2 = open(addr+"temp.txt","r",encoding="utf-8")
    #print(f2.read())
    f2c = f2.read()
    f2.close()
    title = re.findall("<h1\>(.+)</h1\>",f2c)[0]
    if not os.path.exists(addr+title):
        os.mkdir(addr+title)
    #2021.8.28日志:出现了奇怪的错误，f2.read()作为参数被重复调用时，
    #后续出现读取的内容为空的情况，
    #故使用f2c代替
    pic_url = re.findall("<img class=\"vimg\" src=\"(.+)\"\><",f2c)
    #print(pic_url)
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
    url = input("Input Url:")
    get_info(url)
    withdraw_address(0)
    os.system("pause")


if __name__ == "__main__":
    main()
