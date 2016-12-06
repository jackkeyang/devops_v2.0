#!/usr/bin/env python
#encoding=utf8

from flask import request
from utils.dbUtil import *
from utils.public import *
import json

@app.route("/job")