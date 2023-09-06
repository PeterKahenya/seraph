from mongoengine import connect,Document,StringField,ListField
connect("seraph")

class Schema(Document):
    title = StringField(required=True, max_length=200)
    description = StringField(required=False, max_length=200)
    fields = ListField(StringField(max_length=100))