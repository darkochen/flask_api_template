import os
from datetime import datetime
from flask import Flask, request, render_template, send_from_directory, redirect
import json
app = Flask(__name__, static_url_path='')


@app.route('/')
def show():

    date_time = request.args.get("dt")
    fmt = request.args.get("fmt")
    if not date_time:
        date_string = datetime.now().strftime("%Y%m%d%H")
        # return "input time: ?dt=YYYYMMDDHH <br> ex: %s?dt=%s"%(request.url, date_string)
        return redirect("%s?dt=%s"%(request.url, date_string), code=302)
    report_dir = "../report/%s/%s"%(date_time[:8], date_time[8:10])

    user_dict = {}
    for dirname, dirnames, filenames in os.walk(report_dir):
        # print type(dirname)
        if len(dirnames) > 0:
            for d in dirnames:
                # print d
                user_dict[str(d)] = []
            continue
        user_dir = dirname.rsplit("/", 1)[1]
        file_list = []
        for f in filenames:
            file_obj = {}
            f_arr = f.split(".")
            f_uri = f_arr[0]
            f_time = f_arr[1]
            f_run_time = f_arr[2]
            file_obj["method"] = f_uri.split("_", 1)[0]
            file_obj["uri"] = (f_uri.split("_", 1)[1]).replace("_","/")
            file_obj["date"] = f_time.split("_", 1)[0]
            file_obj["time"] = f_time.split("_", 1)[1].replace("_",":")
            file_obj["run_time"] = f_run_time
            file_obj["orig_path"] = dirname
            file_obj["orig_file"] = f
            file_list.append(file_obj)
        user_dict[user_dir] = file_list
    
    if fmt:
        return json.dumps(user_dict)
    return render_template('show.html', user_dict=user_dict, date_time=date_time)


@app.route('/report')
def report():
    path = request.args.get("path")
    file_name = request.args.get("name")
    return send_from_directory(path, file_name)
