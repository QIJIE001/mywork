# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


def jia(x,y):
    return x + y
def jian(x,y):
    return x - y
def chen(x,y):
    return x * y
def chu(x,y):
    return x / y
num1=int(input("请输入第一个数字："))
num2=int(input("请输入第二个数字："))A
choice = input("输入你的符号")
if  choice== '+':
    print('结果为：',num1,'+',num2,'=',jia(num1,num2))
elif  choice== '-': 
    print('结果为：',num1,'-',num2,'=',jian(num1,num2))
elif  choice== '*': 
    print('结果为：',num1,'*',num2,'=',chen(num1,num2))
elif  choice== '/': 
    print('结果为：',num1,'/',num2,'=',chu(num1,num2))
else:
   print("输入符号错误（只有加减乘除哦~）")
    
    
    



    
    