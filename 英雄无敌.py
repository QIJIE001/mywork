print('****************************************************')
print('******************��ӭ����Ӣ���޵�*********************')
print('****************************************************')

xuezhi=100
gongjili=10
fangyuli=50

map=['#','#','#','#','#','#','#']
i=0

name=input('���У��������Ϸ�����������ϷID��')
if not name:
    name='���һ'
print('��Ϸid���óɹ�')
shuxin=[name,xuezhi,gongjili,fangyuli]
print('��ӭ��ң�',name,'�����ѪֵΪ��',xuezhi,',������Ϊ��',gongjili,',������Ϊ��',fangyuli)


print('��Ϸ�����밴d,����a,���ϰ�w,���°�s,�˳�����quit')
while 1:
    map[i]='*'
    print("".join(map))
    userinput=input('ѡ����')

    if userinput=='d' and i < 6:
        map[i]='#'
        i+=1
    elif userinput=='a' and i > 0:
        map[i] = '#'
        i -= 1
    elif userinput=='quit':
        print('�˳���Ϸ')
        break
    else:
        print('')












