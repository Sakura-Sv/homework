#-*- encoding:'utf-8' -*-
import requests
import urllib
import os
from bs4 import BeautifulSoup

def SearchInBaiDuBaiKe():
    print("**************************************************")
    print("******                                      ******")
    print("******  接下来我们将在百度百科中搜索你输入的词  ******")
    print("******                                      ******")
    print("******  同时稍后您可以选择是否存储在文本文件中  ******")
    print("******                                      ******")
    print("**************************************************"+'\n')

    #向百度百科发起请求并爬取数据，解析数据
    name=input("请输入您想查询的词")
    name_url="https://baike.baidu.com/item/"+urllib.parse.quote(name)
    headers={"User-Agent":"User-Agent:Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.70 Safari/537.36;"}
    res = requests.get(name_url,headers=headers).content
    soup = BeautifulSoup(res, 'lxml',from_encoding='utf-8')

    cache = open("./cache.txt","w",encoding="utf-8")

    #输出并打印
    for parat in soup.select('.para'):
        print((repr(parat.get_text())).replace("\\n",""))
        cache.write((repr(parat.get_text()).replace("\\n","")))
        cache.write('\n')

    # 判断是否保存
    while (True):
        f = input('Would you like to save it in a txt file?（Y/N）')
        if f.capitalize() == 'Y' or f.capitalize() == "Yes":
            f = True
            fw = open("./" + name + ".txt", 'w', encoding='utf-8')
            cache=open("./cache.txt","r",encoding="utf-8")
            fw.write(cache.read())
            break
        elif f.capitalize() == 'N' or f.capitalize() == "No":
            f = False
            break
        else:
            print("Your input is wrong, please try it again")
            print("Only Y, Yes, N, No is ")

    #删除缓存文件
    if os.path.exists("./cache.txt"):
        cache.close()
        os.remove("./cache.txt")

    #询问是否继续请求
    f=input("Would you like to search another word?")
    if f.capitalize() == 'Y' or f.capitalize()=="Yes":
        SearchInBaiDuBaiKe()
    elif f.capitalize() == 'N' or f.capitalize()=="No":
        return
    else:
        print("Your input is wrong, please try it again")
        print("Only Y, Yes, N, No is ")

SearchInBaiDuBaiKe()
