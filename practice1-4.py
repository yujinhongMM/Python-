# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 09:44:50 2019

@author: YJH
"""
#百钱买百鸡
for num1 in range(0,21):
    for num2 in range(0,34):
            if 5*num1+3*num2+(100-num1-num2)/3.0==100.0:
                print('鸡翁=',num1,"母鸡=",num2,"小鸡=",100-num1-num2)
