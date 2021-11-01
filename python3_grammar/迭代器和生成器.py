"""
迭代器（iteration)
    __iter__()
    __next__()
    和for循环相似，是一个能够记住访问位置的对象，从集合第一个元素开始，直到元素被访问结束
    只能向前不能后退
    next()方法，实际是在调用__next__


生成器（generation）
    yeild
    生成器保留函数当前运行状态，下次运行时，从上一个yeild处开始运行

[i for i in range(10)]      #链表表达式
(i for i in range(10))      #生成器表达式
生成器表达式比链表表达式节省内存
"""


# 生成器函数实例
def generation_test():
    print('第一次yeild')
    yield 'fisrt'

    print('第二次yeild')
    yield 'second'


# 每次可以去一个值，不用等range(100)完才取值，
# 和generation_b()函数不同，需要等for循环完才能取值
def generation_a():
    for i in range(100):
        yield i


def generation_b():
    ret = []
    for i in range(100):
        ret.append(i)

    return ret


if __name__ == '__main__':
    # [i for i in range(10)]    #链表表达式，
    g_list = (i for i in range(10))  # 生成器表达式
    print(g_list.__next__())
    print(g_list.__next__())

    # 调用生成器
    result_g = generation_test()
    print(result_g)  # 输出结果 <generator object generation_test at 0x0000020EDD827848>
    print(result_g.__next__())  # 输出 第一次yeild  fisrt，保留当前状态
    print(result_g.__next__())  # 输出 第二次yeild  second，本次运行时，函数运行从 yeild 'first' 处开始

    # 下面两次输出结果相同，因为generation_test()每次都重新运行。
    print(generation_test().__next__())
    print(generation_test().__next__())

    result_gen_a = generation_a()
    print(result_gen_a.__next__())  # 取一个值
    print(result_gen_a.__next__())
