# encoding:utf-8
"""
@time:2021/9/121:08
@desc:
    迭代器
"""

# list、tuple、dict、set都是可迭代的对象，可以从他们中获取迭代器（iterator），
# 即：可以使用iter()方法来获取迭代器:  使用 iter()
list_a = iter([1, 2, 3, 4, 5])
tuple_a = iter((1, 2, 3, 4, 5))
dict_a = iter({1: 1,
               2: 2,
               3: 3,
               4: 4,
               5: 5})
set_a = iter({1, 2, 3, 4, 5})

for i in range(5):
    print(next(list_a))
    print(next(tuple_a))
    print(next(dict_a))
    print(next(set_a))

# 同样的字符串也能使用iter()方法获取迭代器
string_a = iter('abcdef')
for i in range(5):
    print(next(string_a))

"""
创建迭代器
    必须包含__iter__()、__next__()两个方法，他们两个共同组成迭代器协议，具体作用：
    __iter__():返回迭代器对象本身；
    __next__():从容器中返回下一项，如果已经没有任何返回，则会引发StopIteration异常。
"""


# 创建一个返回数字的迭代器，从1开始，然后每个序列加1（例如：1，2，3，4，5...）
class Itera_pratice():

    def __init__(self):
        pass

    def __iter__(self):
        self.a = 1
        return self         # 返回本身

    def __next__(self):
        if self.a < 20:
            x = self.a
            self.a += 1
            return x
        else:       # 在迭代的停止条件满足时，使用StopIteration，即：可以使用StopIteration语句来表明迭代完成
            raise StopIteration


itera_p = iter(Itera_pratice())     # 同样的需要使用iter()方法
for i in range(6):
    print(f"迭代器练习：{next(itera_p)}")

