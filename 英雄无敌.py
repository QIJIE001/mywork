print('****************************************************')
print('******************欢迎来到英雄无敌*********************')
print('****************************************************')

xuezhi=100
gongjili=10
fangyuli=50

map=['#','#','#','#','#','#','#']
i=0

name=input('大佬，给你的游戏起个响亮的游戏ID：')
if not name:
    name='玩家一'
print('游戏id设置成功')
shuxin=[name,xuezhi,gongjili,fangyuli]
print('欢迎玩家：',name,'。你的血值为：',xuezhi,',攻击力为：',gongjili,',防御力为：',fangyuli)


print('游戏向右请按d,向左按a,向上按w,向下按s,退出输入quit')
while 1:
    map[i]='*'
    print("".join(map))
    userinput=input('选择方向：')

    if userinput=='d' and i < 6:
        map[i]='#'
        i+=1
    elif userinput=='a' and i > 0:
        map[i] = '#'
        i -= 1
    elif userinput=='quit':
        print('退出游戏')
        break
    else:
        print('')












