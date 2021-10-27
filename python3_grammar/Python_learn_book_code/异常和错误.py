"""
try工作原理：

1.开始try运行后，python在try处做一个标记，当try的子代码出现错误时，就开始返回标记处。

2.并开始和后面except处的异常错误进行匹配，匹配成功后，就运行匹配处的子代码。

3.当没有匹配成功异常，就将异常递交到上层的try，或者到层序的最上层（打印处默认的出错信息）。

4.如果在try子代码没有出现错误，者将执行else中的代码。
"""
try:
    pass
except ValueError:
    pass
except IndexError:
    pass
else:
    pass