"""
Class(类)，
方法：类中定义的函数
类变量：类变量在整个实例化的对象中是公用的。
"""

class Student:

    pub_arg = 'USA'
    def __init__(self,name,sorce):      #变量初始化
        self.name = name
        self.sorce = sorce

    def print_arguemt(self):
        print(self.name)
        print(self.sorce)

S = Student('Tom','First')          #类实例化，输出 <__main__.Student object at 0x000001A96EC05B88>
# print(S)
S.print_arguemt()      #调用类中的方法
Student('Tom','First').print_arguemt()

Student.pub_arg = 'China'       #修改类中变量
# print(Student.pub_arg)

Student.pop = 'cc'          #增加类变量
# print(Student.pop)


del Student.pop     #删除变量

print(Student.__dict__)

#类中增加函数
#新建一个函数
def S_del(self):
    print('from S_del')

#新建一个类中的函数，将新建的函数赋值过去
Student.del_s = S_del

print(Student.__dict__)       #__dict__ 查看数据类型的相关属性

Student.del_s('aaa')