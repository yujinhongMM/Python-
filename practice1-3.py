# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:44:50 2019

@author: YJH
"""
import math
def sushu(n): #判断n是否素数，返回逻辑值
    temp=math.sqrt(n)
    for j in range(2,int(temp)+1):
        if n%j==0:
            return False
    else:
            return True
def main():
    sum=0
    for i in range(2,1000):
        if sushu(i):
            sum=sum+i
    print("1000以内素数和为",sum)

main()
