print('小于1000并且是3和5的倍数的数的和')
b=[]
for i in range(1,1000):
 if i % 3==0 or i % 5==0 :
    b.append(i)
print(b)
d=[]
d=sum(b)
print(d)