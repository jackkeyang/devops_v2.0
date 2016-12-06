#!/usr/bin/env python
#coding:utf-8

from flask import session,render_template,request
from . import app
from utils.public import *

@app.route("/")
@login_required
def index():
    return my_render("index.html")
