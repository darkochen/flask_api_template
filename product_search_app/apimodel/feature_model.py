from flask_restplus import fields
from product_search_app.restplus import api

###########################
##  Request Model
#########################

action_post_request = api.model('action_post_request', {
    'id': fields.Integer(description='id'),
})


###########################
#  Response Model
##########################
response_body = api.model('header', {
        'response_code': fields.Integer(required=True, description='response code: =1 is success; <1 is fail'),
        'response_msg': fields.String(required=True, description='response message'),
})


category_obj = api.model('category_obj',{
        'id': fields.Integer(required=True, description='id'),
        'name': fields.String(required=True, description='name'),
})       

action_post_response = api.inherit('action_post_response', response_body, {
    'response_data' : fields.Nested(category_obj)
}) 


action_get_response = api.inherit('action_get_response', response_body, {
    'response_data' : fields.List(fields.Nested(category_obj))
}) 
