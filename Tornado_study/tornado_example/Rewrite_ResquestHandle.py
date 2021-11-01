# encoding:utf-8
"""
@time:2021/11/122:36
@desc:
    重写 ResquestHandle
"""

import tornado.web
from tornado.concurrent import run_on_executor
from concurrent.futures import ThreadPoolExecutor


class RewriteResquestHandle(tornado.web.RequestHandler):
    executor = ThreadPoolExecutor(4)

    def set_default_headers(self) -> None:
        # 设置在回应时的附加首部
        self.set_header('content-Type', 'application/json')
        self.set_header('Access-Control-Allow-Headers', 'x-requested-with, access_token')
        self.set_header('Access-Control-Allow-Methods', 'POST,GET')
        self.set_header('Access-Control-Max-Age', '3600')

    def post(self):
        ret = yield self.work()
        self.finish(ret)

    @run_on_executor()
    def work(self):
        return True
