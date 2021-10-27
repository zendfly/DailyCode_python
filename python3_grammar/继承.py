"""

"""

class Parentclass1():

    def __init__(self,name,sex):
        self.name = name
        self.sex = sex


class Parentclass2():

    def __init__(self,namea,sexa):
        self.namea = namea
        self.sexa = sexa


class Child(Parentclass1): #单继承
    pass

class Child_a(Parentclass1,Parentclass2): #多继承，继承类大于等于两个
    pass


if __name__ == '__main__':
    
    C1 = Child('a','b')
    print(C1.__dict__)
    print(C1.name)
    print(C1.sex)


    C2 = Child_a('a','b')
    print(C2.__dict__)
    print(C2.namea)
    print(C2.sexa)