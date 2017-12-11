import os
import sys
import urllib
from flask_sqlalchemy import SQLAlchemy
from flask_pymongo import PyMongo
from sqlalchemy.orm import sessionmaker
from flask import Flask, Blueprint, render_template, request
from utils.infralog import InfraLog
from utils.apibase import ApiBase
from product_search_app.restplus import api, app_settings, create_connection_string, api_request_handler
app = Flask(__name__, instance_relative_config=True)
URL_PREFIX = "/%s"%(app_settings.PROJECT_NAME)

def configure_app(flask_app):
    flask_app.config.from_object('config')
    flask_app.config.from_pyfile("config.py", silent=True)
    
    flask_app.config['SWAGGER_UI_DOC_EXPANSION'] = app_settings.RESTPLUS_SWAGGER_UI_DOC_EXPANSION
    flask_app.config['RESTPLUS_VALIDATE'] = app_settings.RESTPLUS_VALIDATE
    flask_app.config['RESTPLUS_MASK_SWAGGER'] = app_settings.RESTPLUS_MASK_SWAGGER
    flask_app.config['ERROR_404_HELP'] = app_settings.RESTPLUS_ERROR_404_HELP
    sqlalch_conn_dict = create_connection_string(app.config['PROJ_DATABASE_CONFIG'])
    flask_app.config['SQLALCHEMY_BINDS'] = sqlalch_conn_dict
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = app_settings.SQLALCHEMY_TRACK_MODIFICATIONS
    flask_app.config["SQLALCHEMY_POOL_RECYCLE"] = app_settings.SQLALCHEMY_POOL_RECYCLE
    
    flask_app.config["PROJ_BASE_DIR"] = os.path.abspath(os.path.join(os.path.dirname(__file__) , ".."))
    # flask_app.config["SQLALCHEMY_RECORD_QUERIES"] = True
    # flask_app.config['SQLALCHEMY_ECHO'] = True

    # if multiple databases 
    # for db_name, db_value in app.config['PROJ_MONGO_CONFIG'].iteritems():
    #     for key, value in db_value.iteritems():
    #         flask_app.config['%s_%s'%(db_name, key)] = value


def initialize_app(flask_app):
    blueprint = Blueprint('api', __name__, url_prefix=URL_PREFIX)
    api.init_app(blueprint)
    flask_app.register_blueprint(blueprint)
    

def create_app(app):
    initialize_app(app)
    return app


configure_app(app)
InfraLog.Setup(
    ident=app.config["LOG_IDENT"], \
    device=eval(app.config["LOG_DEVICE"]),\
    priority=InfraLog.Priority(app.config["LOG_PROIORITY"]),\
    project=app.config["LOG_IDENT"],
    log_path=app.config["LOG_PATH"] if app.config["LOG_PATH"] is not "."\
        else os.path.abspath(os.path.join(os.path.dirname(__file__) , ".."))
)
alchemy_db = SQLAlchemy(app)
mongo_client = PyMongo(app)
# if multiple databases 
#mongo_vds3 = PyMongo(app, config_prefix='VDS3')
session = sessionmaker()
api_request_handler(app, InfraLog)
from product_search_app.webapi.featureA import ns as ex_namespace
create_app(app)



