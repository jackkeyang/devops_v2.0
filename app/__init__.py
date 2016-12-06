from flask import Flask
from config import *

app = Flask(__name__)
app.config.from_object(config["dev"])
app.secret_key = app.config.get("SECRET_KEY",None)
salt = app.config.get("SALT",None)

import login,index,usermanage,idc,project,job