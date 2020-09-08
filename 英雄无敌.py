print('****************************************************')
print('******************欢迎来到英雄无敌*********************')
print('****************************************************')

xuezhi=100
gongjili=10
fangyuli=50

map=[['#','#','#'],['#','#','#'],['#','#','#']]
i=0
j=0
x = 0               #定义x 轴 y轴坐标
y = 0

name=input('大佬，给你的游戏起个响亮的游戏ID：')
if not name:
    name='玩家一'
print('游戏id设置成功')
shuxin=[name,xuezhi,gongjili,fangyuli]
print('欢迎玩家：',name,'。你的血值为：',xuezhi,',攻击力为：',gongjili,',防御力为：',fangyuli)


print('游戏向右请按d,向左按a,向上按w,向下按s,退出输入quit')

map[x][y] = "*"
for i in map:
    for j in i:
        print(j, end=" ")
    print()
while True:
    userinput = input("选择方向：")
    if userinput=="d" and y<3:         # 右
        y+=1
    elif userinput=="a" and y>0:       # 左
        y-=1
    elif userinput=="s" and x<3:       # 下
        x+=1
    elif userinput == "w" and x > 0:   # 上
        x -= 1
        
    map = [['#','#','#'],['#','#','#'],['#','#','#']]
    map[x][y] = "*"
    for i in map:
        for j in i:
            print(j,end=" ")
        print()

    

    
