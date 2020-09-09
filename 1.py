class Student(object):
   
    def __init__(self, name, age):
        self.__name = name    
        self.__age = age      

    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age

stu = Student('柒杰', 22)
print("姓名：%s"%(stu.get_name()))
print("年龄：%s"%(stu.get_age()))