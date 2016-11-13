#!/usr/bin/env python
#coding:utf-8

from . import app
from flask import request
from utils.dbUtil import *
from utils.public import *
import json

@app.route("/idc")
@login_required
def idclist():
    fields = ["id", "name", "name_cn", "address"]
    data = DB().get_list("idc", fields)
    return my_render("/asset/idc.html",idcs=data)

@app.route("/idcadd",methods=["GET","POST"])
@login_required
def idcadd():
    if request.method == "GET":
        return my_render("/asset/idcadd.html")
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())

        add_idc = {}
        add_idc["name"] = data["name"]
        add_idc["address"] = data["address"]
        idcs = DB().get_list("idc",["name","address"])

        if add_idc in idcs:
            return json.dumps({"code":1,"errmsg":"机房已存在"})

        DB().create("idc",data)
        return json.dumps({"code":0,"result":"机房添加成功"})

@app.route("/idcupdate",methods=["GET","POST"])
@login_required
def idcup():
    if request.method == "GET":
        id = request.args.get("id")
        data = DB().get_one("idc",["id","name","name_cn","address"],{"id":id})
        return json.dumps(data)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        DB().update("idc",data)
        return json.dumps({"code":0})

@app.route("/idcdel",methods=["POST"])
@login_required
def idcdel():
    id = request.form.get("id")
    DB().delete("idc",{"id":id})
    return json.dumps({"code":0})