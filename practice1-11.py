# -*- coding: utf-8 -*-
"""
Created on Thu Apr 11 11:25:26 2019

@author: YJH
"""

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
    headers = {                            #加个请求头伪装浏览器
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36"
    }
    try:
        r = requests.get(url, headers=headers)
        r.raise_for_status()
        r.encoding = r.apparent_encoding
        print('success')
        return r.text
    except:
        print('false')
        return 'false'

        
#解析超文本，提取所需数据
def getInfo(html):
    '''
    html:待解析的
    '''
    unifo=[]#存放提取的数据，用于返回数据
    soup = BeautifulSoup(html, 'lxml')
    lis = soup.find_all('li', {"class":"gl-item"})
    print(len(lis))
    for i in range(len(lis)):
        try:
            # 获取商品信息 div 中的第一个 a 标签， 获取 title 属性值
            title = lis[i].a['title']
            # print(title)
            # 获取商品的价格信息
            price = lis[i].find('div', class_='p-price').i.string
            # print(price)
            unifo.append([title, price])
        except:
            print('')
    return unifo


# 显示数据
def displayHtmlGoods(goods_data):
    std = r'{0:^100}{1:^8}'
    print(std.format('商品名称', '价格'))
    with open('data.txt','w') as f:    #设置文件对象
        for i in range(len(goods_data)):
            f.write(std.format(goods_data[i][0], goods_data[i][1])+"\n")                 #将字符串写入文件中
            print(std.format(goods_data[i][0], goods_data[i][1]))

    
def main():
    
    url_basic = 'https://search.jd.com/Search?keyword='
    total_pages = 1 # 需要爬取的总页数
    keyword = '电脑' # 关键字


    for i in range(total_pages):
        page = 1 + i * 2 
        url = url_basic + keyword + '&enc=utf-8&wq=' + keyword + '&page=' + str(page)
        print(url)
        html = getHtml(url)
        MyInfo=getInfo(html)
  
    displayHtmlGoods(MyInfo)


main()
