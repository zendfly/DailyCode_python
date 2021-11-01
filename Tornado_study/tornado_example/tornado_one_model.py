# encoding:utf-8
"""
@time:2021/11/122:57
@desc:
    使用tornado接受图片，并调用model进行推理
"""
import cv2
import json

import tornado
from tornado.concurrent import run_on_executor

from Tornado_study.tornado_example.model_infer import Model_infer
from Tornado_study.tornado_example.Rewrite_ResquestHandle import RewriteResquestHandle


class OneModelResquestHandle(RewriteResquestHandle):

    def initialize(self, model):
        self.model = model

    @tornado.gen.coroutine
    def post(self):

        final_result = {}

        try:

            file_metas = self.request.files
            info = file_metas['file'][0]
            img = info['body']
            img = cv2.imdecode(img, cv2.IMREAD_COLOR)

            ret = yield self.detection(img, final_result)

            self.finish(ret)
        except Exception as e:

            ret = json.dumps(final_result)
            self.finish(ret)

    @tornado.concurrent.run_on_executor()
    def detection(self, image, final_result):

        infer_result = Model_infer().run(image)

        return json.dumps(infer_result)
