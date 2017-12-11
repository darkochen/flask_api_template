FROM python:2.7

RUN apt-get update \
    && apt-get -y install vim wget 


RUN pip install Flask==0.11.1
RUN pip install flask-restplus==0.9.2
RUN pip install Flask-SQLAlchemy==2.1
RUN pip install Flask-Script==2.0.5
RUN pip install gunicorn==19.6.0
RUN pip install gevent==1.2.1
RUN pip install mysql-connector-python-rf==2.2.2
RUN pip install flask-pymongo==0.4.1

ADD . /opt/product_search
WORKDIR /opt/product_search

CMD tail -f /dev/null
