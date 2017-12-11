# initialization your project
- ```./initialization_project.sh your_project_name```
- ```ex: ./initialization_project.sh abc```

# install environment
- check local folder have in  docker-compose.volumes
- ```docker-compose up -d```

# run service
- Swagger API Document:
-- ```http://127.0.0.1:1085/```

# local run, install environment
- ```pip install virtualenv```
- create virtualenv and install packages by using the following command:

-- ```virtualenv venv``` or ```source venv/bin/activate```
-- ```pip install -r requirements.txt```

- run debug mode api service
-- ```python run_debug.py```

- run server mode
-- ```gunicorn -c gunicorn_config.py product_search_app.app:app```

- --Swagger API Document: http://127.0.0.1:8085/product_search
 
# use cProfile run
 - ```gunicorn -c cProfile/gunicorn_config_cProfile.py product_search_app.app:app```
 - run cProfile report `python cProfile/report_site/run_web.py `
 -- http://127.0.0.1:8090/
 - gunicorn_config_cProfile Setting:
 -- GEN_REPOST_SEC: More than the number of seconds to generate the report
