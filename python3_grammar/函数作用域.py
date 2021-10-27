"""
函数——变量作用域
    指该变量可以在程序中被引用的范围
"""

#exp
def foo():
    name = 'foo a'
    print(name)
    def in_def():
        name = 'in in_def a'
        print(name)

    return in_def

if __name__ == '__main__':
    a = foo()()
    # a()
