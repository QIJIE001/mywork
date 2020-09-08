

import random,string 
str="".join(random.sample(string.ascii_letters+string.digits,4))
print("随机四位验证码:",str)
print("生成的列表为:",list(str)) 