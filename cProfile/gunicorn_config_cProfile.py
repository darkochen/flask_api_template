from multiprocessing import cpu_count

def get_workers():
    return cpu_count() / 3 + 1

bind = '0.0.0.0:8085'
capture_output = True
workers = get_workers()
worker_class = "gevent"
#thread = 2
preload_app = True # init one instance
graceful_timeout = 60
loglevel = 'info'
accesslog = 'access_log.log'
access_log_format = '%({X-Real-IP}i)s %({X-Forwarded-For}i)s %({authorization}i)s | %(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s" **%(L)s/%(D)s**'
errorlog = 'error_log.log'

#######################################################
import sys
import cProfile
import pstats
import StringIO
import os
import time
import datetime

PROFILE_LIMIT = int(os.environ.get("PROFILE_LIMIT", 200))
PROFILER = bool(int(os.environ.get("PROFILER", 1)))
GEN_REPOST_SEC = 5

def profiler_enable(worker, req):
    worker.profile = cProfile.Profile()
    worker.profile.enable()
    worker.log.info("PROFILING %d: %s" % (worker.pid, req.uri))

def profiler_summary(worker, req, environ, total_time):
    s = StringIO.StringIO()
    worker.profile.disable()
    file_name = gen_file_name(req, environ, total_time)
    print >> sys.stderr, file_name
    if file_name:
        ps = pstats.Stats(worker.profile, stream=open(file_name, 'w')).sort_stats('time', 'cumulative')
    else:
        ps = pstats.Stats(worker.profile, stream=s).sort_stats('time', 'cumulative')
    ps.print_stats(PROFILE_LIMIT)
    print >> sys.stderr, "[%s] [cProfile] %s" % (req.uri, unicode(s.getvalue()))

def pre_request(worker, req):
    worker.start_time = time.time()
    if PROFILER is True:
        profiler_enable(worker, req)

def post_request(worker, req, environ):
    total_time = time.time() - worker.start_time
    print >> sys.stderr, "\n[%d] [cProfile] [%s] URI %s | Load Time: %.3fs" %\
        (worker.pid, req.method, req.uri, total_time)
    if PROFILER is True and ("webapi" in req.uri.lower()) and total_time >= GEN_REPOST_SEC:
        profiler_summary(worker, req, environ, total_time)

def gen_file_name(req, environ, total_time):
    user = ""
    try:
        if "HTTP_VDSUSER" in environ and environ["HTTP_VDSUSER"] is not None:
            user = environ["HTTP_VDSUSER"].replace(" ", "_")
        if not user and "HTTP_AUTHORIZATION" in environ:
            user = environ["HTTP_AUTHORIZATION"].replace("Bearer ","")
        if not user:
            user = "unknown"
    except Exception as e:
        print >> sys.stderr, "[error] [cProfile] %s" % (e)
        user = "unknown"
    file_name = "%s_%s"%(req.method, req.uri)
    file_name = "%s.%s.%s.%s"%( \
        file_name.replace("/","_"), \
        datetime.datetime.fromtimestamp(int(time.time())).strftime('%Y-%m-%d_%H_%M_%S'), \
        int(total_time),\
        int(time.time() * 1000000))
    date_time = (datetime.datetime.utcnow() + datetime.timedelta(hours=+8)).strftime("%Y%m%d %H")\
        .split(" ")

    file_dir = "%s/report/%s/%s/%s"%(os.path.abspath(os.path.join(os.path.dirname(__file__))),\
        date_time[0], date_time[1], user)
    try:
        if not os.path.exists(file_dir):
            os.makedirs(file_dir)
    except IOError, e:                
        print >> sys.stderr, "[error] [cProfile] os.makedirs error - %s"%(e)
        return None
    
    return "%s/%s.txt"%(file_dir, file_name)
