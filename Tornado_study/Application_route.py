# encoding:utf-8
"""
@time:2021/10/2723:31
@desc:
    Tornado_study web Application 下的URL路由
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


app = Application(
    [url('r', MainHandler),
     url('/story/([0-9]+)', StoryHandler, dict(db=db), name='Story')]
)


