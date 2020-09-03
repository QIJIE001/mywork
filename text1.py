# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:03:58 2020

@author: tute
"""
a=[]
print('随意输入一个值，把值保存为一个列表，输入q结束')
while 1:
    i=input('请输入数值：')
    if i=='q':
        break
    a.append(i)
    print(a)
    
