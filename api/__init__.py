from flask import Flask,request,abort
from markupsafe import escape

app = Flask(__name__)

@app.get("/")
def seraph():
    return "<h1>Welcome to Seraph </p>"