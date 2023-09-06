from flask import Flask,request,abort
from markupsafe import escape
from .db import Schema


app = Flask(__name__)


@app.get("/")
def seraph():
    return "<h1>Welcome to Seraph </p>"


@app.get("/schema")
def get_schemas():
    return Schema.objects.to_json()


@app.post("/schema")
def add_schema():
    title = request.json["title"]
    description = request.json["description"]
    fields = request.json.get("fields",[])
    schema = Schema()
    schema.title = title
    schema.description = description
    schema.fields = fields
    schema.save()
    return schema.to_json()

