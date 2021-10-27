"""
高阶函数
定义：
    1、函数接受的参数为一个函数名
    2、函数的返回值为一个函数名
    3、满足以上任意一点就为高阶函数
"""
#exp,test()高阶函数
# def foo():
#     print('hellow')
#
# #高阶函数，参数为函数名
# def test(func):
#     print(func)     #输出的时func的地址
#     func()      #调用运行func函数
#
# test(foo)
#
# #返回值为函数名
# def test_a(foo):
#     pass
#     return foo


"""
函数嵌套下
在函数内部再创建一个函数
"""
#exp
# def out_func():
#
#     def inner_func():
#         pass


"""
闭包
在嵌套函数中，嵌套的函数中变量取值，从里层向外层寻找。和变量作用域类似
"""
# def fater(name):
#     name_c = 'cc'
#     def sun():
#         name_a = 'bb'
#         def grandsun():
#             # print(name)
#             # print(name_a)
#             # print(name_c)
#         grandsun()
#     sun()
#
# fater('aaa')

"""
装饰器，@
本质是一个函数，功能是为被装饰函数添加辅助功能
原则：不能修改被装饰函数的源代码，不能修改被装饰函数的调用方式
"""

import time

#统计函数运行时间
def count_time(func):

    def in_time(*args,**kwargs):        # *args,**kwargs 表示所有参数
        """
        :param args:  *args，表示一个数量不定的参数，以元组方式传递
        :param kwargs:  *kwargs，表示一个数量不定的关键字参数，以字典方式传递
        :return: 返回c的结果
        """
        start_time = time.time()
        c = func(*args,**kwargs)
        stop_time = time.time()
        print('运行时间为%s'%(start_time - stop_time))
        return c
    return in_time

#装饰器,相当于 f_test = count_time(f_test),执行in_time(),
@count_time
def f_test():
    s = 0
    for i in range(10):
        s =+ i
    print(s)
    return 'from f_test %s'%s

print(f_test())