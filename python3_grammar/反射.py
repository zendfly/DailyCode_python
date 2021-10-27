"""
反射，python的一种自省（自查）方式，有四种方法
    hasattr()       #返回对象是否具有给定名称的属性，hasattr(*args, **kwargs)
        *args：类名
        *kwargs：属性名
        :return  Ture  False。Return whether the object has an attribute with the given name

    getattr()       #检查类中是否有该属性,getattr(object, name, default=None)
        object：被检查的类
        name：检查的属性名，以字符串形式 ' '
        :return :<function FtpCline.maxa at 0x000001A45732E4C8>

    setattr()       #将给定对象上的命名属性设置为指定值，setattr(x, y, v)
        setattr(x, y, v) 相当于 x.y = v
        Sets the named attribute on the given object to the specified value


    delattr()       #删除给定对象上中的指定的属性，delattr(x, y)
        delattr(x, y) 相当于 del x.y
"""

class FtpCline():

    def __init__(self,name,maxc):
        self.name = name
        self.maxc = maxc

    def trans(self):
        print('传输')

    def acc(self):
        print('接收')


if __name__ == '__main__':

    """
        hasattr(*args, **kwargs)       #返回对象是否具有给定名称的属性
            *args：类名
            *kwargs：属性名
            :return  Ture  False。Return whether the object has an attribute with the given name
    """
    Ft = FtpCline('alxe','100')
    res_hasattr = hasattr(Ft, 'maxa')     #False
    res_hasattr_a = hasattr(Ft,'trans')       #Ture
    print(res_hasattr)
    print(res_hasattr_a)


    """
        getattr(object, name, default=None)       #检查类中是否有该属性
            object：被检查的类
            name：检查的属性名，以字符串形式 ' '
            default = None，当没有指定的属性时的返回值
            :return :<function FtpCline.maxa at 0x000001A45732E4C8>
    """
    res_gettart = getattr(Ft,'se','没有这个属性')         #当没有给定的属性时，返回默认值
    print(res_gettart)
    res_gettart_a = getattr(Ft,'trans')       #return: <function FtpCline.trans at 0x00000193CA616EE8>，实例，可以直接运行
    print(res_gettart_a)
    res_gettart_a()


    """
        setattr(x, y, v)       #将给定对象上的命名属性设置为指定值
            setattr(x, y, v) 相当于 x.y = v
            Sets the named attribute on the given object to the specified value
            既可以设定数据属性，也可以设定函数属性
    """
    setattr(Ft,'Set_va','test')     #设定数据属性
    print(Ft.__dict__)

    setattr(Ft,'func',lambda x:x-1)     #设定函数属性
    print(Ft.func(10))


    """
        delattr(x, y)       #删除给定对象上中的指定的属性
            delattr(x, y) 相当于 del x.y
    """
    delattr(Ft,'Set_va')
    print(Ft.__dict__)
