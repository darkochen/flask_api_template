#!/usr/bin/python
# -*- coding: utf-8 -*-
import httplib


class RespCodeMap():
    exists_same_picture = 72
    call_api_fail = 71
    download_from_url_fail = 70
    not_found_package = 51
    package_exist = 50
    successfully_exception = 2
    no_content = 3
    recognition_status_fail = 4
    successfully = 1
    param_error = -1
    del_data_error = -2
    request_entity_too_large = -3
    illegal_file_format = -5
    bad_request = -6
    undefined_error = -999

# error code and msg map
err_map = { 
    RespCodeMap.exists_same_picture: ("exists_same_picture", httplib.OK),
    RespCodeMap.call_api_fail: ("call_api_fail", httplib.OK),
    RespCodeMap.download_from_url_fail: ("download from url fail", httplib.OK),
    RespCodeMap.not_found_package: ("not found package", httplib.OK),
    RespCodeMap.package_exist: ("package exist", httplib.OK),
    RespCodeMap.successfully_exception: ("Successfully, Have exception", httplib.OK),
    RespCodeMap.no_content: ("No content", httplib.NO_CONTENT),
    RespCodeMap.recognition_status_fail: ("Recognition status fail", httplib.OK),
    RespCodeMap.successfully: ("Successfully", httplib.OK),
    RespCodeMap.param_error: ("param error", httplib.BAD_REQUEST),
    RespCodeMap.undefined_error: ("Handle, Undefined", httplib.OK),
    RespCodeMap.del_data_error: ("Error on deleting data", httplib.BAD_REQUEST),
    RespCodeMap.request_entity_too_large: ("Request entity too large", httplib.REQUEST_ENTITY_TOO_LARGE),
    RespCodeMap.illegal_file_format: ("ILLEGAL FILE FORMAT", httplib.BAD_REQUEST),
    RespCodeMap.bad_request: ("Bad request", httplib.BAD_REQUEST)
}
