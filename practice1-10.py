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


#coding=utf-8

### 导入包
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

### 获取数据
def getData(sFilePath):
    csv_file = pd.read_csv(sFilePath)
    csv_file = csv_file[['year', 'month','day','pm2.5', 'TEMP', 'PRES', 'Iws']]
    # print(csv_file.head(5))

    ## 1. 统计每年, 日均 PM2.5, 日均气温
    q1 = csv_file[['year', 'pm2.5', 'TEMP']]
    q1 = q1.groupby('year').mean()

    ## 2. 统计5年内PM2.5, 气温, 气压, 累计降雨量
    q2 = csv_file[['year','pm2.5', 'TEMP', 'PRES', 'Iws']]
    q2 = q2.groupby('year').sum()
    # print(q2)

    ## 3. PM2.5每年平均最高5个月, 获取每天的PM2.5的指数
    q3 = csv_file[['year','month','day','pm2.5']]
    print(q3.head(5))

    ## 返回数据
    return q1, q2, q3


### 获取第一个问题的数据,画出柱状图
def draw1(q1):
    # 处理数据
    q1_pm25 = np.array(q1['pm2.5']).tolist()
    q1_TEMP = np.array(q1['TEMP']).tolist()
    print(q1)
    print(q1_pm25)
    print(q1_TEMP)
    # 设置标签
    years = ['2010', '2011', '2012', '2013', '2014']
    # 设置并列的宽度
    total_width, n = 0.4, 1
    width = total_width/n
    # 处理每个柱状的宽度
    x_pm25 = list(range(len(q1_pm25)))
    x_temp = list(range(len(q1_TEMP)))
    for i in range(len(x_pm25)):
        x_temp[i] = x_pm25[i] + width

    #画图
    plt.rcParams['font.sans-serif'] = ['SimHei']
    plt.bar(x_pm25, q1_pm25, width=width, label ='PM2.5', tick_label=years, fc='b')
    plt.bar(x_temp, q1_TEMP, width=width, label='Temperature',tick_label=years, fc = 'y')
    plt.xlabel('年份')
    plt.title('PM2.5 以及 温度的每年每天平均值柱状图')
    plt.legend()
    plt.show()

### 获取第二个问题的数据,画出折线图
def draw2(q2):
    # 处理数据
    q2_pm25 = np.array(q2['pm2.5']).tolist()
    q2_temp = np.array(q2['TEMP']).tolist()
    q2_pres = np.array(q2['PRES']).tolist()
    q2_iws = np.array(q2['Iws']).tolist()
    print(q2_pm25)
    print(q2_temp)
    print(q2_pres)
    print(q2_iws)
    # 设置标签
    years = ['2010', '2011', '2012', '2013', '2014']

    # 设置子图2*2
    plt.rcParams['font.sans-serif'] = ['SimHei']
    # PM2.5
    plt.subplot(221)
    plt.plot(years, q2_pm25)
    plt.title('PM2.5')
    plt.xlabel('年份')
    plt.ylabel('pm2.5的值')
    # 温度
    plt.subplot(222)
    plt.plot(years, q2_temp)
    plt.title('温度')
    plt.xlabel('年份')
    plt.ylabel('年温度总和')
    # 气压
    plt.subplot(223)
    plt.plot(years, q2_pres)
    plt.title('气压')
    plt.xlabel('年份')
    plt.ylabel('年气压总和')
    # 降雨量
    plt.subplot(224)
    plt.plot(years, q2_iws)
    plt.title('降水量')
    plt.xlabel('年份')
    plt.ylabel('年降水量')

    # 画图
    plt.show()

### 获取第三个问题的数据, 画出折线图
def draw3(q3):
    colors = ['yellow', 'orange', 'red', 'gray', 'pink']
    # 首先需要获得年份的数据
    years = np.array(q3.groupby(['year']).size().index);
    # 获取当年每个月平均值的排序,然后描写最高月的点
    for year in years:
        cur_ydata = q3.loc[q3['year']==year, ['month', 'day', 'pm2.5']]
        mon_mean = cur_ydata.groupby(['month'])['pm2.5'].mean().sort_values(ascending=False)
        max_month=mon_mean.index[:5]
        days = 0
        pm_values = []
        for mon in max_month:
            mon_data = cur_ydata.loc[cur_ydata['month'] == mon, ['day', 'pm2.5']]
            mon_ddata_mean = mon_data.groupby(['day'])['pm2.5'].mean()
            days += mon_ddata_mean.size # 计算当月总天数
            pm_values += list(mon_ddata_mean.values)
        plt.plot(range(days), pm_values, color=colors[year%len(colors)], label=str(year))
    plt.legend()
    plt.xlabel('day')
    plt.ylabel('pm2.5')
    plt.show()

if __name__ == "__main__":
    sFilePath = '.\\pollution.csv'
    q1, q2, q3 = getData(sFilePath)
    draw1(q1)
    draw2(q2)
    draw3(q3)