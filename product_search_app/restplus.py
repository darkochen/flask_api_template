from flask_restplus import Api
from product_search_app.etc import app_settings
from flask import Flask, request

api = Api(version='1.0', title='%s API'%(app_settings.PROJECT_NAME),
          description='%s Flask RestPlus powered API'%(app_settings.PROJECT_NAME))

def create_connection_string(db_params):
    db_connection_string = {}
    for db_name in db_params:
        db_config = db_params[db_name]
        if db_config['CONNSTR'] == 'mysql+mysqlconnector':
            connection_string = "%s://%s:%s@%s:%s/%s?charset=utf8" \
                % (db_config['CONNSTR'], db_config['USERNAME'], db_config['PASSWORD'],\
                   db_config['HOST'], db_config['PORT'], db_config['DBNAME'])
 
            db_connection_string[db_name] = connection_string
        else:
            print >> sys.stderr, " !!! ERROR in [%s] -> \n Not Support this 'connstr'='%s'"\
                % (__file__, db_config['connstr'])
    return db_connection_string

def api_request_handler(app, ilg):
    
    @app.before_first_request
    def before_first_request():
        pass

    @app.before_request
    def before_request():
        ilg.Write(ilg.PRI_INFO, "**API Start : %s"%(request.url_rule))

    @app.after_request
    def after_request(response):
        ilg.Write(ilg.PRI_INFO, "**API End : %s"%(request.url_rule))
        return response

#@api.errorhandler
#def default_error_handler(e):
#    message = 'An unhandled exception occurred.'
#    log.exception(message)
#
#    if not app_settings.FLASK_DEBUG:
#        return {'message': message}, 500
#
#
#@api.errorhandler(NoResultFound)
#def database_not_found_error_handler(e):
#    log.warning(traceback.format_exc())
#    return {'message': 'A database result was required but none was found.'}, 404
