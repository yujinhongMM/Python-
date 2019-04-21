# -*- coding: utf-8 -*-
"""
Created on Thu Mar 21 10:46:34 2019
简单爬虫————request+beautifulsoup
@author: YJH
"""
import requests
from bs4 import BeautifulSoup 
#获取指定url的超文本
def getHtml(url):
    '''
    url:需要爬数据的网络地址
    '''
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status() #如果r.status_code不等于200，产生http访问异常
        r.encoding=r.apparent_encoding
        return(r.text)
    except:
        print("访问目标页面异常")
        
#解析超文本，提取所需数据
def getInfo(html):
    '''
    html:待解析的
    '''
    unifo=[]#存放提取的数据，用于返回数据
    '''
    soup=BeautifulSoup(html,'html.parser')  
    for tr in soup.find('tbody').children:#得到表格中的所有行
        if isinstance(tr.bs4.element.Tag):
            tds=tr('td')    #得到当前行的所有列(含标签、属性、值)
            unifo.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
    '''
    soup=BeautifulSoup(html)
    for tbody in soup.find_all('tbody', { "class" : "tbody-container" }):
        for tr in tbody.find_all('tr'):#得到表格中的所有行
            tds=tr('td')    #得到当前行的所有列(含标签、属性、值)
            unifo.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string,tds[4].string])
    return unifo

    
if __name__ == "__main__":
    url="http://www.gaokaopai.com/paihang-otype-2.html?f=1&ly=bd&city=&cate=&batch_type="
#   filename="datal.csv"
    html=getHtml(url)
    MyInfo=getInfo(html)
#    saveData=(MyInfo)
    print(MyInfo)
    
