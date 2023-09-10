from flask import Flask,request,abort
from markupsafe import escape
from .db import *


app = Flask(__name__)


@app.get("/")
def seraph():
    return "<h1>Welcome to Seraph </p>"

@app.get("/fields")
def get_fields():
    return FIELD_TYPES


@app.get("/schema")
def get_schemas():
    return Schema.objects.to_json()


@app.post("/schema")
def add_schema():
    title = request.json["title"]
    description = request.json["description"]
    schema = Schema()
    schema.title = title
    schema.description = description
    
    fields = request.json.get("fields",[])
    for f in fields:
        field_cls = eval(f['_cls'])
        field = field_cls(**f)
        schema.fields.append(field)
    
    schema.save()
    return schema.to_json()

