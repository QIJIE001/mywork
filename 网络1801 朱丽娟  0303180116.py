# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""




import random,string 
ran_str="".join(random.sample(string.ascii_letters+string.digits,4))
print("随机产生的四位验证码是:",ran_str)
print("列表为:",list(ran_str))   