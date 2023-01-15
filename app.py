# -*- coding: utf-8 -*-
"""
Created on Tue Nov 15 15:21:18 2022

@author: laksh
"""

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"