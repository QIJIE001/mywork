# -*- coding: utf-8 -*-
"""
Created on Thu Sep  3 11:25:48 2020

@author: tute
"""


sum1=0
sum2=0
a=[]
b=[]

game1=input('请输入一队的名字：')
game2=input('请输入二队的名字：')
while 1:
    c1=int(input('请输入一队的成绩：'))
    a.append(c1)
    sum1=sum(a)
    print(game1,'的成绩为：',sum1)
    c2=int(input('请输入二队的成绩：'))
    b.append(c2)
    sum2=sum(b)
    print(game2,'的成绩为：',sum2)
    c=input('继续请回车，结束请输入：game over')
    if c=='game over':
        if sum1>sum2:
            print('球队',game1,'胜利,当前比分为：',sum1,':',sum2)
        elif sum1 == sum2:
             print('球队',game2,'与',game2,'平局,当前比分为：',sum1,':',sum2)
        else:
            print('球队',game2,'胜利,当前比分为：',sum1,':',sum2)
        break




    
