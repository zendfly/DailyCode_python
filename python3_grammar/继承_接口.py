"""
接口：实质是一个函数
接口——继承：继承的类需要实现被继承类中定义的方法
"""
import abc      # Abstract Base Classes，作用：在代码中定义和使用抽象基类进行API检查。


class file(metaclass=abc.ABCMeta):  #定义一个基类

    # 定义接口函数
    @abc.abstractmethod
    def write(self):
        pass

    @abc.abstractmethod
    def read(self):
        pass


class memary_file(file):        #接口-继承，memary_flie类需要实现file类中的函数方法

    def __init__(self):
        pass

    def write(self):
        print('write')

    def read(self):
        print('read')