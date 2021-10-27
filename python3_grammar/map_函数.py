"""
map()，
    map(func,list)
    :return 迭代器（一个可迭代对象）
    func:函数
    list:可迭代随想

reduce()
    reduce(func(x,y),[list1,list2])
    #使用传入的func()函数，操作[list1,list2]中的参数
"""

#map()，参数有f()和参数
def add_1(i):
    return i + 1

def map_test(func,arr):

    ret = []
    for i in arr:
        c = func(i)
        ret.append(c)
    return  ret


#reduce()，和map()相似，但使用两个参数
def add_2(x,y):
    return x+y

def reduce_test(func,arr):

    ret1 = []
    for i in range(len(arr)):
        res = func[arr[i],arr[i+1]]
        ret1.append(res)

    return ret1

if __name__ == '__main__':
    list1 = [1,2,3,4,5]
    res = map(add_1,list1)
    print(list(res))

