#!/usr/bin/python
# -*- coding: utf-8 -*-

import os
import sys
from datetime import datetime as dt

from sqlalchemy import Column, ForeignKey, func
from sqlalchemy.dialects.mysql import BIT, INTEGER, SMALLINT, VARCHAR, NVARCHAR\
     , TIMESTAMP, DATETIME
from sqlalchemy.orm import relationship, backref
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class AdCategory(Base):
    __tablename__ = 'ad_category'

    id = Column('id', INTEGER, primary_key=True, nullable=False, autoincrement=True)
    name = Column('name', VARCHAR(255), nullable=False)
    name_zh_tw = Column('name_zh_tw', VARCHAR(45), nullable=False)
    name_zh_cn = Column('name_zh_cn', VARCHAR(45), nullable=False)
    valid = Column('valid', SMALLINT)
    created_time = Column("created_time", DATETIME, nullable=False, default=dt.utcnow)
    dfp_name = Column("dfp_name", VARCHAR(45))


# test
def showObj(obj):
    for property, value in vars(obj).iteritems():
        print property, ": ", value

def obj2dict(model):
    if model is None:
        return None
 
    return {col.name: getattr(model, col.name) for col in model.__table__.columns}
 
 
def listobj2dict(model_list):
    if model_list is None:
        return None
 
    res = []
    for i in model_list:
        res.append(obj2dict(i))
    return res 


def main():
    sys.path.insert(0, os.path.join("..",".."))

    #import json
    import datetime
    from product_search_app.app import app, alchemy_db
    app.app_context().push()
    
 
    #from sqlalchemy import create_engine
    #engine = create_engine(connection_string)

    engine = alchemy_db.get_engine(alchemy_db.get_app(), "VDS3")
    
    from sqlalchemy.orm import sessionmaker
    session = sessionmaker()
    session.configure(bind=engine)
    s = session()
    
    cst = s.query(TagModelEntity).filter(
        TagModelEntity.model_id == 1
    ).first()

    # print listobj2dict(cst)
    print cst
    showObj(cst)

    # resList = []
    # for i in cst:
    #     resList.append(obj2dict(i))

    # print resList



if __name__ == "__main__":
    sys.exit(main())
