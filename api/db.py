from mongoengine import connect,Document,StringField,ListField,IntField,EmbeddedDocumentField,EmbeddedDocument
import math
import sys


connect("seraph")


FIELD_TYPES = []


class SeraphFieldType(EmbeddedDocument):
    meta = {'allow_inheritance': True}
    field_type = StringField(required = True, max_length=200,default="")
    field_name = StringField(required = True, max_length=200, default="")
    field_key = StringField(required = True, max_length=200,default="")
    field_description = StringField(required = True, max_length=2000,default="")
    
    def __init__(self, *args, **kwargs):
        super(SeraphFieldType, self).__init__(*args, **kwargs)


class SeraphIntegerField(SeraphFieldType):
    max_value = IntField(default = sys.maxsize)
    min_value = IntField(default = -sys.maxsize)

    def __init__(self, *args, **kwargs):
        super(SeraphIntegerField, self).__init__(*args, **kwargs)
        self.field_type = "Integer"


class SeraphStringField(SeraphFieldType):
    max_length = IntField(default = 1000)
    min_length = IntField(default = 1)

    def __init__(self, *args, **kwargs):
        super(SeraphStringField, self).__init__(*args, **kwargs)
        self.field_type = "String"


class Schema(Document):
    title = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=200)
    fields = ListField(EmbeddedDocumentField(SeraphFieldType))

import json
FIELD_TYPES.append(json.loads(SeraphIntegerField().to_json()))
FIELD_TYPES.append(json.loads(SeraphStringField().to_json()))

