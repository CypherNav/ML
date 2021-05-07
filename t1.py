import threading
import time

import flask
from werkzeug.utils import html
r1=threading.Lock()
r2=threading.Lock()
from flask import Flask,render_template
app=Flask(__name__)
@app.route("/<int:count>")
def home(count):
    return render_template("check.html",stars=count)

if __name__=="__main__":
    app.run(use_reloader=True,debug=True)


