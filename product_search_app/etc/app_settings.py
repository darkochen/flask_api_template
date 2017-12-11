#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys

# Flask-Restplus settings
RESTPLUS_SWAGGER_UI_DOC_EXPANSION = 'list'
RESTPLUS_VALIDATE = True
RESTPLUS_MASK_SWAGGER = False
RESTPLUS_ERROR_404_HELP = False
SQLALCHEMY_TRACK_MODIFICATIONS = False
SQLALCHEMY_POOL_RECYCLE = 30

PROJECT_NAME = "product_search"

print >> sys.stderr, " --------------read config done, %s ----------------" % (__file__)
