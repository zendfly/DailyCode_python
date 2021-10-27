"""
静态属性
    @property，将class中方法变成数据属性。隐藏中间的处理过程

    当类调用方法时（不创建实例时，调用类中的方法）
    @classmethod，变成类使用的方法，自动传递参数

    @staticmethod，静态方法只是名义上归属类管理，不能使用变量和实例变量，是类的工具包
"""

class Student():

    targ = 'targe'
    def __init__(self,a,b,c):
        self.a = a
        self.b = b
        self.c = c

    @property   #变成数据属性
    def add_a(self):
        return self.a + self.b

    @classmethod    #将方法变成类方法，自动传递参数
    def teat_a(cls):
        print(cls)
        print(cls.targ)

    @staticmethod   #静态方法，
    def wash_baby():
        print('test')


if __name__ == '__main__':
    """
    将方法变成类的数据属性，可以直接调用
    """
    s = Student(1,2,3)
    print(s.add_a)  #经过property装饰器后，和调用class的数据属性一样
    print(s.a)
    print(s.b)

    """
    将方法变成类方法
    """
    Student.teat_a()        #使用classmethood后，可以不用将class实例化（创建实例）后进行直接调用
