#!/usr/bin/env python
# vim:fileencoding=utf-8

import os
import sys
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world!!"

if __name__ == "__main__":
    app.run()