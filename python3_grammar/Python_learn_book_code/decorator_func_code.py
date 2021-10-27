"""
装饰函数（function decorator），也称装饰函数， @方法名
    装饰器可以对被装饰函数进行扩展，也对可以返回一个对象
    装饰函数的参数要有函数
    class Foo()
        pass

    @Foo    # 相等于  Foo(Ftt)
    def Ftt()
        pass


"""


#记录函数调用次数
class Tranc:
    """
    当func调用时，触发__call__方法
    """
    def __init__(self,func):
        self.func = func
        self.calls = 0

    def __call__(self, *args):
        self.calls += 1

        print('call %s to %s ' %(self.calls,self.func.__name__))
        self.func(*args)


@Tranc      #相等于 Tranc(Spam)
def Spam(a,b,c):
    print(a,b,c)

@Tranc
def Spam1(a):
    print(a)

# Spam(1,2,3)
# Spam('a','b','c')
# Spam(4,5,2)
# Spam1(1)

###############  装饰器返回一个对象  ###################
def counts(aClass):
    aClass.numInstances = 0
    return aClass

@counts
class Span():

    def __init__(self):
        pass

    def p1(self):
        pass

    def p2(self):
        pass

print(Span)
print(Span)
print(Span)
