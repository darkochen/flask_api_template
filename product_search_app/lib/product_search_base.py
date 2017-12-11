#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os
import traceback

sys.path.insert(0, os.path.join(os.path.dirname(__file__) , "..", ".."))
from product_search_app.app import app, app_settings, InfraLog as Ilg, alchemy_db, mongo_client
from product_search_app.utils.sqlalchemyutil import SqlAlchemyUtil
from product_search_app.entity.vds3entities import AdCategory

class ExampleBase:
    reload(sys)
    sys.setdefaultencoding('utf-8')

    def __init__(self):
        try:
            self._db = SqlAlchemyUtil()
            self._dbname = "VDS3"
          
        except Exception as e:
            Ilg.Write(Ilg.PRI_ERROR, e)
        return
    
    def get_category(self):
        with self._db.session_scope(self._dbname) as session:
            result = session.query(AdCategory).filter().all()
        return result

    def upd_category(self):
        with self._db.session_scope(self._dbname) as session:
            result = session.query(AdCategory).filter().first()
            result.valid = 1
        return result    

    def get_mongo(self):
        result = mongo_client.db.ads.find_one(
            {
                'video_id': 35,
            }
        )
        return result


def main():
    from product_search_app.app import app
    app.app_context().push()

    r = ExampleBase()
    # print r.get_category()
    # print r.get_mongo()
    print r.upd_category()

if __name__ == "__main__":
    sys.exit(main())
