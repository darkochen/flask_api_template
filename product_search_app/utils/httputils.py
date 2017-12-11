#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import requests


class HttpUtil(object):
    
    @staticmethod
    def http_request(method, url, data, headers={'Content-Type': 'application/json'}):
        _header = headers.copy()     
        if method.lower() == 'get':
            if "Content-Type" in _header:
                del _header["Content-Type"]
            response = requests.get(url, data=data, headers=_header)
        if method.lower() == 'post':
            response = requests.post(url, data=data, headers=headers)
        if method.lower() == 'patch':
            response = requests.patch(url, data=data, headers=headers)            
        return response

    @staticmethod
    def http_upload(url, files, data="", headers={}):
        response = requests.post(url, files=files, data=data, headers=headers)
        return response
