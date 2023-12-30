import flask
from flask import Flask, request
import os

app = Flask(__name__)

@app.route('/')

def this_works():
  return "This works..."

if  __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
