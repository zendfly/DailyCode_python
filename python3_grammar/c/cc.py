

class CC():

    def __init__(self):
        pass

    def pf(self):
        print('from c_CC_class')

    def _test(self):
        print('from c.CC test')



def _picvated_attr():
    print('函数名前加 _ 表示私有函数，使用 import * 不能导入')