"""
调用继承的父类需要
使用super()，调用继承的父类
"""
class List(list):

    def append(self, object):
        #两种调用父类方法的方式
        list.append(self,object)
        # super().append(object)        #使用super()，可以省略self，并不用关心父类名字

c = List('hellow ')
# print(c)
c.append('1111')
print(c)
