# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 11:18:51 2020

@author: tute
"""

j=int(input('请输入一个数字：'))
from random import randrange
print(j)
i=randrange(0,100,1)
print(i)
if j<i:
     print('输入的数字比随机数小')    
elif j>i:
     print('输入的数字比随机数大')
elif j==i:
     print('输入的数字比随机数一样')
else:
     print('输入错误')
   
