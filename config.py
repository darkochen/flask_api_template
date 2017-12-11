# -*- conding: utf-8 -*-
import os
import sys
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


PROJ_DATABASE_CONFIG = {
    "VDS3" : {
        "CONNSTR": "mysql+mysqlconnector",
        "HOST": "192.168.7.55",
        "PORT": "3336",
        "USERNAME": "root",
        "PASSWORD": "1qaz2wsx",
        "DBNAME": "vds3"
    }
}
SQLALCHEMY_POOL_SIZE = 10
SQLALCHEMY_MAX_OVERFLOW = 20

# if multiple databases 
PROJ_MONGO_CONFIG = {
    # "VDS3": {
    #     "HOST": "192.168.7.55",
    #     "PORT": "27317",
    #     "USERNAME": "root",
    #     "PASSWORD": "1qaz2wsx",
    #     "DBNAME": "vds3"
    # }
}

MONGO_URI = "mongodb://root:1qaz2wsx@192.168.7.55:27317/vds3"
MONGO_MAX_POOL_SIZE = 100

LOG_IDENT = "product_search"
LOG_DEVICE = "InfraLog.DEV_FILE|InfraLog.DEV_SYSLOG|InfraLog.DEV_CONSOLE "
LOG_PROIORITY = "DEBUG"
#LOG_PATH = "/opt/var/%s"%(LOG_IDENT)
LOG_PATH = "."


print >> sys.stderr, " --------------read config done, %s ----------------" % (__file__)

