"""
匿名函数
lambda 参数：表达式

"""

#普通函数
def add_one(x):
   return x+1


#高阶函数
def h_func(func,arry):
    new_list = []
    for i in arry:
        new_list.append(func(i))
    return new_list


if __name__ == '__main__':

    list = [1,2,3,4,5]
    print(h_func(add_one,list))
    print(h_func(lambda x:x+1,list))        #匿名函数，和map()函数作用相似



