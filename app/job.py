#!/usr/bin/env python
#encoding=utf8

from . import app
from utils.public import *
from utils.dbUtil import *
from flask import request
import json

fields = ["id","job_type","job_info","apply_name","apply_date","deal_time","deal_persion","status"]

@app.route("/jobadd",methods=["GET","POST"])
@login_required
def jobadd():
    if request.method == "GET":
        return my_render("/job/jobadd.html")
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        nowtime = myTime().nowtime()
        apply_name = session.get("username")
        data.setdefault("apply_date",str(nowtime))
        data.setdefault("apply_name",apply_name)
        DB().create('jobs',data)
        return json.dumps({"code":0,"result":"工单申请成功"})

@app.route("/joblist/")
@login_required
def joblist():
    where = {'status':['0','1']}
    data = DB().get_list("jobs",fields,where)
    for ondata in data:
        ondata["apply_date"] = myTime().nowtimestr(ondata["apply_date"])
    return my_render("/job/joblist.html",jobs=data)

@app.route("/jobhistory/")
@login_required
def jobhistory():
    data = DB().get_list("jobs",fields)
    for ondata in data:
        ondata["apply_date"] = myTime().nowtimestr(ondata["apply_date"])
        if ondata["deal_time"]:
            ondata["deal_time"] = myTime().nowtimestr(ondata["deal_time"])
    return my_render("/job/jobhistory.html",jobs=data)

@app.route("/jobupdate",methods=["POST"])
@login_required
def jobupdate():
    data = dict((k,v[0]) for k,v in dict(request.form).items())
    deal_persion = session.get("username")
    deal_time = myTime().nowtime()
    data.setdefault("deal_persion",deal_persion)
    data.setdefault("deal_time",deal_time)
    DB().update("jobs",data)
    return json.dumps({"code":0})

@app.route("/jobdetail")
@login_required
def jobdetail():
    id = request.args.get("id")
    data = DB().get_one("jobs",fields,{"id":id})
    print data
    return json.dumps(data)