# -*- coding: utf-8 -*-
"""
Created on Mon Mar 11 22:04:46 2019

@author: YJH
"""
"""
value=[50,20,10,5,1]#纸币面额

def main():
    while(1):
       x=eval(input("小汽车金额:"));
       if x<=0:
           print("不能小于等于0");
       else:
           break;
    while(1):
       z=eval(input("购买小汽车数:"));
       if z<=0:
           print("不能小于等于0");
       else:
           break;
    while(1):
       y=eval(input("用户支付金额:"));
       if y<x*z:
           print("你给的钱不足！");
       else:
           break;
    d=y-x*z;
    num=0;
    if(d<100):
        if(d>=value[0]):
            d=d-50;
            num=num+1;
        if(d>=value[1]):
            num=num+d/20;
            d=d-20*d/20;
        if(d>=value[2]):
            d=d-10;
            num=num+1;
        if(d>=value[3]):
            d=d-5;
            num=num+1;
    num=num+d;
    print("需要张数：",num);

main()
"""


value = [100,50,20,10,5,1]
num = [0,0,0,0,0,0]
def change_money(x):
    sum=0
    for i in range(len(value)):
        num[i] = x // value[i] #取整除 - 返回商的整数部分（向下取整）	
        sum=sum+num[i]
        x = x % value[i]
    
    return sum

def main():
    while(1):
       x=eval(input("小汽车金额:"));
       if x<=0:
           print("不能小于等于0");
       else:
           break;
    while(1):
       z=eval(input("购买小汽车数:"));
       if z<=0:
           print("不能小于等于0");
       else:
           break;
    while(1):
       y=eval(input("用户支付金额:"));
       if y<x*z:
           print("你给的钱不足！");
       else:
           break;
    print("找零张数为：",change_money(y-x*z))
    print("分别为：")
    for i in range(len(value)):
         print(value[i],"元",num[i],"张")
main()
