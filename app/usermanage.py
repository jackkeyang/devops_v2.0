#!/usr/bin/env python
#coding:utf-8

from . import app
from flask import request
from utils.dbUtil import *
from utils.public import *
import json
import hashlib

salt = app.config.get("SALT")

@app.route("/userlist",methods=["GET","POST"])
@login_required
def userlist():
    users = DB().get_list("user",["id","username","cn_name","email","phone","role","status"])
    return my_render("userlist.html",users=users)

@app.route("/getuser",methods=["GET","POST"])
@login_required
def getuser():
    if request.method == "GET":
        userid = request.args.get("id")
        user = DB().get_one("user",["id","username","cn_name","email","phone","role","status"],{"id":userid})
        return json.dumps(user)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        print data
        DB().update("user",data)
        return json.dumps({"code":0})

@app.route("/cgpasswd",methods=["POST"])
@login_required
def cgpasswd():
    data = dict((k,v[0]) for k,v in dict(request.form).items())

    if len(data) == 4:
        old_passwd = DB().get_one("user",["password"],{"id":data["id"]})
        data["oldpasswd"] = hashlib.md5(data["oldpasswd"]+salt).hexdigest()
        if data["oldpasswd"] != old_passwd["password"]:
            return json.dumps({"code":1,"errmsg":"密码错误"})
        else:
            data.pop("oldpasswd")

    if not data["password"]:
        return json.dumps({"code":1,"errmsg":"密码不能为空"})
    if data["password"] != data["re_password"]:
        return json.dumps({"code":1,"errmsg":"两次输入密码不同"})

    data.pop("re_password")
    data["password"] = hashlib.md5(data["password"]+salt).hexdigest()
    print data
    DB().update("user",data)
    return json.dumps({"code":0,"result":"密码修改成功"})



@app.route("/adduser",methods=["GET","POST"])
@login_required
def adduser():
    if request.method == "GET":
        return my_render("adduser.html")
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        if data["password"] != data["re_password"]:
            return json.dumps({"code":1,"errmsg":"两次密码不同"})
        if DB().get_one("user",["username"],{"username":data["username"]}):
            return json.dumps({"code":1,"errmsg":"用户已存在"})

        data.pop("re_password")
        data["password"] = hashlib.md5(data["password"] + salt).hexdigest()
        DB().create("user",data)
        return json.dumps({"code":0})

@app.route("/deluser",methods=["POST"])
@login_required
def deluser():
    id = request.form.get("id")
    DB().delete("user",{"id":id})
    return json.dumps({"code":0})

@app.route("/ucenter",methods=["GET","POST"])
@login_required
def ucenter():
    if request.method == "GET":
        name = session.get("username")
        fields = ["id","username","cn_name","email","phone","role","status"]
        user = DB().get_one("user",fields,{"username":name})
        return my_render("ucenter.html",user=user)
    else:
        data = dict((k,v[0]) for k,v in dict(request.form).items())
        DB().update("user",data)
        return json.dumps({"code":0,"result":"用户信息修改成功"})