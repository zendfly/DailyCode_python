"""
    __getattr__、__setattr__、__delattr__ python内置属性，
    当我们需要写自己的属性时，可以对其进行重新定义，实现自己需要的逻辑
    __getattr()__   #在调用属性不存在时，触发，
        当我们调用不存在的属性时，Python会自动报错，
        但我们对__getattr()__进行修改后，会返回我们想要的结果，并不会提示报错

    __delattr()__   #在删除属性时，触发

    __setattr()__   #在设定属性时，触发

    __delattr()__、__setattr__，用处较少
"""

class Foo():

    def __init__(self,name):
        self.name = name

    def pr(self):
        print('from %s'%self.name)

    def __getattr__(self, item):
        print('调用的%s不存在'%item)

    #当对类进行实例化时，触发。但在类的属性字典没有任何属性
    def __setattr__(self, key, value):
        # print('设置属性')
        # print(key,value)
        # 对设置的属性进行类型检查
        if type(value) is str:  #是否是str
            self.__dict__[key] = value      #对类属性字典进行设置
        else:
            print('设定的属性类型错误')

    #对类属性的删除进行控制，当进行删除是，触发，并执行下面操作
    def __delattr__(self, item):
        print('%s不能删除'%item)

        # self.__dict__.pop(item)     #在属性字典中进行删除


foo = Foo('alax')
print(foo.__dict__)
print(dir(foo))   #查看foo中内置的属性
print(foo.x)    #调用不存在的属性，触发__getattr__

#删除
del foo.name
print(foo.__dict__)
