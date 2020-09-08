print('****************************************************')
print('******************欢迎来到英雄无敌*********************')
print('****************************************************')


map=[['#','#','#'],['#','#','#'],['#','#','#']]

x = 0
y = 0


def add_user():
name=input('请设置游戏ID：')
password=input('请设置游戏密码：')



if not name:
    name='玩家一'
print('游戏id设置成功')

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
