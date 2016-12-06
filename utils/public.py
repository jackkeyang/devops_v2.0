#!/usr/bin/env python
#coding:utf-8

from flask import session,redirect,render_template,url_for
from functools import wraps
import time,datetime

def login_required(func):
    @wraps(func)
    def deco(*args,**kwargs):
        if not session.get('username'):
            return redirect(url_for("login"))
        else:
            return func(*args,**kwargs)
    return deco

def my_render(*args,**kwargs):
    return render_template(info=session,*args,**kwargs)

class myTime():
    #获取当前时间戳
    def nowtime(self):
        return time.mktime(datetime.datetime.now().timetuple())
    #将时间戳转时间字符串
    def nowtimestr(self,timestr):
        return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(int(timestr)))
