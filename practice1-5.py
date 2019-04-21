# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:44:50 2019

@author: YJH
"""

"""
def f(n):
    if n==1:
        return 1
    if n==2:
        return 2
    if n==3:
        return 4
    else:
        return f(n-1)+f(n-2)+f(n-3)

def main():
    n=eval(input("请输入上山的台阶数目："))
    print("跳法有：",f(n))

main()
"""

def main():
     n=eval(input("请输入上山的台阶数目："))
     sum=0
     if n==1:
        sum=1
     if n==2:
        sum=2
     if n==3:
        sum=4
     t1=1
     t2=2
     t3=4
     for i in range(4,n+1):
         sum=t1+t2+t3
         t1=t2
         t2=t3
         t3=sum
     print("跳法有：",sum,"种")
main()