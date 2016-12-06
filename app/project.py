#!/usr/bin/env python
#encoding=utf8

from flask import request
from utils.dbUtil import *
from utils.public import *
import json

@app.route("/project")
def prolist():
    fields = ["id","app_name","language","soft_version","sys_resource","db_info","other_relation","app_user","dever","test_host","pre_host","real_host"]
    data = DB().get_list("project",fields)
    return my_render("/asset/prolist.html",pros=data)

@app.route("/proup")
def proup():
    id = request.args.get("id")
    fields = ["id","app_purpose","app_name","language","soft_version","sys_resource","db_info","other_relation","app_user","dever","test_host","pre_host","real_host"]
    data = DB().get_one("project",fields,{"id":id})
    return json.dumps(data)