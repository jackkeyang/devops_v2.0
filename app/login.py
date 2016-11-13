#!/usr/bin/env python
#coding:utf-8

from flask import request,render_template,session,redirect,url_for
from . import app
from utils.dbUtil import *
import json
import hashlib

salt = app.config.get("SALT")

@app.route("/login",methods=["GET","POST"])
def login():
    if request.method == "GET":
        return render_template("login.html")
    if request.method == "POST":
        data = dict((k,v[0])for k,v in dict(request.form).items())
        userinfo = DB().get_one("user",["id","username","password","role","status"],{"username":data["name"]})

        data["password"] = hashlib.md5(data["password"]+salt).hexdigest()

        if not userinfo:
            return json.dumps({"code":1,"errmsg":"用户不存在"})
        if data["password"] != userinfo["password"]:
            return json.dumps({"code":1,"errmsg":"密码错误"})
        if userinfo["status"] == 1:
            return json.dumps({"code":1,"errmsg":"用户被锁定"})

        session["username"] = userinfo["username"]
        session["role"] = userinfo["role"]
        return json.dumps({"code":0})

@app.route("/logout/")
def logout():
    session.pop("username")
    session.pop("role")
    return redirect(url_for("login"))