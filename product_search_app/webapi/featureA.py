#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys
import os

from flask import request
from flask_restplus import Resource, reqparse
from product_search_app.app import app, ApiBase, api
from product_search_app.service.featureAservice import FeatureAService
from product_search_app.apimodel.feature_model import action_post_request
from product_search_app.apimodel.feature_model import action_post_response,\
    action_get_response
    
MY_FILE = os.path.basename(__file__).split(".")[0]
ns = api.namespace('webapi/%s'%(MY_FILE), description='%s Service'%(MY_FILE))

_SERVICE_ = FeatureAService()

@ns.route('/1/action')
class Action(Resource, ApiBase):
    _service = _SERVICE_
    parser_get = reqparse.RequestParser()
    parser_get.add_argument('acid', 
        type=int, 
        required=True
        )
    @api.expect(parser_get)
    @api.marshal_with(action_get_response)
    def get(self):
        """ get data list """
        args = self.parser_get.parse_args()
        return self.api_process(self._service.action_get, request,  **args)

    @api.expect(action_post_request)
    @api.marshal_with(action_post_response)
    def post(self):
        """ get data obj """
        return self.api_process(self._service.action_post, request)
        

@ns.route('/2/action/<acid>')
@ns.param('acid', 'vds3.ad_category.id')
class Action2(Resource, ApiBase):
    _service = _SERVICE_
    # @api.marshal_with(product_search_get_response)
    def get(self, acid):
        """ get subcategory list """
        return self.api_process(self._service.action2_get, request)







