# -*- coding: utf-8 -*-
"""
Created on Thu Mar 28 10:34:31 2019

@author: YJH
"""

import pandas as pd
import matplotlib.pyplot as plt

filename = 'pollution.csv'

   
 # 读取训练数据   
df = pd.read_csv(filename,encoding='cp936')  
df =df.dropna()
#生成折线图
plt.figure()
df1=df[:]
df1['day']=df1['date'].map(lambda x:x[:x.rindex('-')])
df1=df1.groupby(by='day',as_index=False).sum()
 df1.plot(x=df1['])

    

