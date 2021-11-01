# encoding:utf-8
"""
@time:2021/10/2723:07
@desc:
"""
import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self):      # get 请求；post 提交
        self.write('Hellow，world')


def make_app():
    return tornado.web.Application(
        [(r"/", MainHandler), ]
    )


if __name__ == '__main__':
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()
