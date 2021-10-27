"""
__import__() :以字符串的形式导入模块，返回值是最顶层的模块
"""

c_module = __import__('c.cc')
print(c_module)     #返回c
c_module.cc.CC().pf()

#以字符串形式导入模块
import importlib

c = importlib.import_module('c.cc')
c.CC()._test()
print(c)

#import * 不能导入私有函数，即 函数名前加 '_'，但可以直接导入
from c.cc import _picvated_attr
_picvated_attr()