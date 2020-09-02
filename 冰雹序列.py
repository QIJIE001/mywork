# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


print('冰雹序列')
i=eval(input('请输入一个数字：'))
while i!=1:
    if i%2==0:
        i=i/2
        print(i)
    elif i%2==1:
        i=i*3+1
        print(i)
