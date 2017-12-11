#!/usr/bin/python
# -*- coding: utf-8 -*-


import os
import sys
import traceback


sys.path.insert(0, os.path.join(os.path.dirname(__file__) , "..", ".."))
from product_search_app.app import app, app_settings, InfraLog as Ilg
from product_search_app.etc.errors_list import RespCodeMap
from product_search_app.lib.product_search_base import ExampleBase


class FeatureAService:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def __init__(self):
        try:
            self._eb = ExampleBase()
        except Exception as e:
            print >> sys.stderr, e
        return

    def action_post(self, **params):
        category_list = self._eb.get_category()
        return category_list[0], RespCodeMap.successfully

    def action_get(self, **params):
        category_list = self._eb.get_category()
        return category_list, RespCodeMap.successfully

    def action2_get(self, **params):
        data = self._eb.get_mongo()
        result = {}
        try:
            result = {
                "uid": data["uid"],
                "content": data["content"]
            }
        except Exception as e:
            Ilg.Write(Ilg.PRI_ERROR, e)

        return result, RespCodeMap.successfully


def main():
    from product_search_app.app import app
    app.app_context().push()

    r = FeatureAService()

    print r.action_post({})
    # print r.product_search_get({})

if __name__ == "__main__":
    sys.exit(main())


