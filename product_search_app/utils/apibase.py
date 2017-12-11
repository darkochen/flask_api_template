#!/usr/bin/python
# -*- coding: utf-8 -*-
import sys
import inspect
import traceback

from demoportal_app.app import InfraLog as Ilg
from demoportal_app.etc.errors_list import err_map, RespCodeMap


class ApiBase(object):

    def service_exception_handle(self, result, e=''):
        Ilg.Write(Ilg.PRI_ERROR, traceback.format_exc())
        result['response_msg'] = str(sys.exc_info()[0])
        result['response_code'] = -99999
        return result

    def api_process(self, func, request, **kwargs):
        result = {}
        status_code = 200
        if request.environ["REQUEST_METHOD"] == "GET":
            params = request.view_args
        else:
            params = request.json
            if params is None:
                params = {}
        params.update(kwargs)
        try:
            ret, result['response_code'] = func(**params)
            default_msg, status_code = err_map.get(result['response_code'], ("Undefined", -9999))

            if result['response_code'] == RespCodeMap.successfully:
                result['response_data'] = ret
                result['response_msg'] = default_msg
            else:
                result['response_data'] = None
                result['response_msg'] = ret if ret else default_msg
        except Exception as e:
            self.service_exception_handle(result)
        return result, status_code


