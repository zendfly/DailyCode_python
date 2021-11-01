# encoding:utf-8
"""
@time:2021/10/2723:02
@desc:
    Tornado_study base handle
    如果在ResquestHandler中需要一些特殊的订制方法，可以自己进行重写。对已存在的方法也可以重写，例如get()、post()方法
"""
import tornado
from tornado.web import RequestHandler


class SelfRquestHandler(RequestHandler):

    pass



