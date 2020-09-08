import sys

print('****************************************************')
print('******************欢迎来到英雄无敌*********************')
print('****************************************************')
map=[['#','#','#'],['#','#','#'],['#','#','#']]
x = 0
y = 0
name_list = open('E:/1.txt','r+')
name_text = dict(line.strip().split(":") for line in name_list if line)
for i in range(3):
    name = input("账号ID:")
    password = input("密码:")
    lock_name = open('E:/2.txt', 'r+')
    # 检测用户是否被锁定
    for j in lock_name.readlines():
        if name == j.strip():
            print("因尝试过多导致{}用户锁定".format(name))
            exit(1)
    # 验证用户名密码是否正确
    if password == name_text.get(name):
        print("欢迎用户{name} 登陆...".format(name=name))
        break
    # 输入两次后用户被锁定，将锁定用户写入2文件中
    elif i == 2:
        lock_name = open('E:/2.txt','a+')
        lock_name.write(name+'\n')
        lock_name.close()
        print("因尝试过多导致{}用户锁定".format(name))
        exit(2)
    else:
        print('''账号或密码输入错误!---------剩余尝试次数:{}---------'''.format(2-i))


if not name:
    name='玩家一'


user_info={"name":name,"xuezhi":100,"gongjili":10,"fangyuli":50,}
print('玩家的信息为：')
for i in user_info:
    print(i,":",user_info[i])

print('开始游戏')
print('游戏规则：向右按d,向左按a,向上按w,向下按s,退出输入quit')

map[x][y] = "*"
for i in map:
    for j in i:
        print(j, end=" ")
    print()
while 1:
    userinput = input("选择方向或者退出：")
    if userinput=="d" and y<2:         # 右
        y+=1
    elif userinput=="a" and y>0:       # 左
        y-=1
    elif userinput=="s" and x<2:       # 下
        x+=1
    elif userinput == "w" and x > 0:   # 上
        x -= 1
    elif userinput == "quit" :   # 退出
        break

    map = [['#','#','#'],['#','#','#'],['#','#','#']]
    map[x][y] = "*"
    for i in map:
        for j in i:
            print(j,end=" ")
        print()



