# Tornado 

Tornado



## Hello World

 Tornado Web应用程序通常由一个或多个RequestHandler的Application子类将传入的请求路由到处理程序的对象，以及main()函数来启动服务。

eg:

```python
# encoding:utf-8
"""
@time:2021/10/2723:07
@desc:
"""
import tornado.ioloop
import tornado.web

# 处理程序
class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('Hellow，world')


def make_app():
    # 使用Application将请求路由到处理程序
    # 下面的return 就是将 "/"请求路由到MainHandler处理程序（Applcation的主要作用就是路由）
    return tornado.web.Application(
        [(r"/", MainHandler), ]			# 这里的路由是元组
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)		# 监听端口
    tornado.ioloop.IOLoop.current().start()

```

Application对象负责全局配置，包括将请求映射到处理程序的映射表。在Application中其实包含了一个路由表。路由表是URLSpec对象（或元组），每个对象至少包含一个正则表达式和一个处理程序类。路由表顺序很重要，按顺序匹配。如果正则表达式包含捕获组，则这些组是**路径参数**并传递给处理程序。

例如，下面例子中，根URL “/” 映射（路由）到MainHandler，表单URL “/story/”后跟一个数字映射到StoryHandler。这个数字（作为字符串）传递给StoryHandler.get.

```python
# encoding:utf-8
"""
@time:2021/10/2723:31
@desc:
    tornado web Application 下的URL路由
"""
from tornado.web import Application
import tornado


class MainHandler(tornado.web.RequestHandler):
    def get(self):
        self.write('----')
        
        
class StoryHandler(tornado.web.RequestHandler):
    def initizalize(self, db):
        self.db = db
        
    def get(self, story_id):
        self.write('this is story %s'%story_id)

# 这里Application的路由是RUL
app = Application(
    [url('r', MainHandler),		
     url('/story/([0-9]+)', StoryHandler, dict(db=db), name='Story')]
)

```

上面代码主要说明，Application子类充当路由，通过正则表达式对请求进行解析，并分配给对应的处理程序。同时，请求还可以当作str类型参数进行传递。

## RequestHandler子类

在写处理函数时继承的RequestHandler，因为Tornado Web应用程序大部分工作都RequestHandler中进行。处理程序子类的主要入口点以：get()，post()等。每个处理程序可以定义一个或者多个这些方法来处理不同HTTP请求。

除了get()、post()方法等，某些其他方法......(未完:20211027)





--参考：https://www.osgeo.cn/tornado/guide/structure.html