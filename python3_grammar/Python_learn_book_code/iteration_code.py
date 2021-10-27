"""
迭代器（iteration），
    __next__
    __iter__
    文件的任何一种形式都是可迭代的
"""

L = [1,2,3]
l1 = iter(L)        #对L进行可迭代化
print(l1.__next__())
print(next(l1))