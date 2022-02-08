from dler import *
import os


def dl_novel(url,file):
    #获取原始网页
    download(url,file,"text")
    html = open(file,"r",encoding = "utf-8")
    content = html.read()
    html.close()

    #指定保存文件
    if os.path.exists(addr+"result.txt"):
        dest = open(addr+"result.txt","a",encoding="utf-8")
    else:
        dest = open(addr+"result.txt","w",encoding="utf-8")

    #提取并写入内容
    title = re.search("(?<=<h1 id=\"atitle\">).+(?=</h1>)",content).group()
    passages = re.findall("((?<=<p>)([^\x00-\xff]|[a-zA-Z0-9\ ])+)",content)
    #此处表达式外面括号匹配一个结果，里面括号匹配一个结果，返回一个元组，分别对应两个结果

    if re.search("（[0-9]{1,2}）",title) == None:
        dest.write(title+"\n")#分节标题不写(没有中文括号才写)
    for each in passages:
        if not (each[0]=="翻上页" or each[0]=="翻下页" or each[0]=="呼出功能"):#正则表达式不完善
            dest.write(each[0]+"\n")

    dest.close()
    print("[SUCCESS]%s"%title)

    #状态码
    if content.find("下一页")!=-1:#一章内的分节
        return True
    elif content.find("下一章")!=-1:#章末
        return False
    #else:#小说结尾
       #return -1
    
def get_catalog(url):#获取章节列表
    download(url,addr + "temp.txt","text")
    with open(addr + "temp.txt","r",encoding="utf-8") as f:
        ulist = re.findall("(?<=<a href=\").+(?=\" class=\"chapter-li-a \">)",f.read())
    iter = 0
    while iter < len(ulist):
        ulist[iter] = "https://w.linovelib.com" + ulist[iter]
        iter+=1
    os.remove(addr+"temp.txt")
    return ulist


if __name__ == "__main__":
    url = input("Input address:")
    urlist = get_catalog(url)
    for u in urlist:#逐章下载
        tsuzuki = dl_novel(u,addr+"temp.txt")
        count = 2
        while tsuzuki:
            tsuzuki = dl_novel(u[:-5]+"_"+str(count)+".html",addr+"temp.txt")
            count+=1

      
