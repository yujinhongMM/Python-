# -*- coding: utf-8 -*-
"""
Created on Sat Mar  9 21:59:32 2019

@author: YJH
"""

w=[0,4,5,2,1,6] #w[i]是物品的重量
v=[0,45,57,22,11,67] #v[i]是物品的价值
n=len(w)-1 
m=8 #背包的容量
x=[False for raw in range(n+1)] #x[i]为True表示物品被放入背包
a=[[0 for col in range(m+1)] for raw in range(n+1)] 
def knap_DP(n,m):
    for i in range(1,n+1):#每一行代表可选择的物品，可选择的物品是自上而下的增多
        for j in range(1,m+1):#每一列代表的是小偷能偷 j kg重的物品时，在行的约束下的最大值
            a[i][j]=a[i-1][j]#这是没放入第i行物品的时候a[i][j]的值
            #比较j与w[i](对于要放物品的重量)，放入物品价值入不放入物品价值的大小，j-w[i]是装入该物品的重量，i-1就是j-w[i]还没装入i行物品的能拿的最大价值
            if(j>=w[i] and (a[i-1][j-w[i]]+v[i]>a[i-1][j])):
                a[i][j]=a[i-1][j-w[i]]+v[i]
    j=m
    for i in range(n,0,-1):
        if a[i][j]>a[i-1][j]:
            x[i]=True
            j=j-w[i]
    
    Mv=a[n][m]
    return Mv

def main():
    print("小偷最多能偷价值",knap_DP(n,m),"的物品")
    print("被偷物品如下：")
    for i in range(0,n+1):
        if(x[i]==True):
            print("重量：",w[i]," 价值：",v[i])

main()
            
            
        