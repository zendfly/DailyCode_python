"""
组合
    将两个class进行关联，把一个类作为参数传入另一个类中
"""


class School():

    def __init__(self,name,addr):
        self.name = name
        self.addr = addr

class Course():

    def __init__(self,name,pice,perion,School): #已类作为参数进行传入，使两个类产生关联
        self.name = name
        self.pice = pice
        self.perion = perion
        self.school = School


if __name__ == '__main__':

    S1 = School('ALi','hangzhou')
    c1 = Course('A','B','C',S1)
    print(c1)
    print(c1.school.name)   #调用类中类数据属性
    print(c1.name)

