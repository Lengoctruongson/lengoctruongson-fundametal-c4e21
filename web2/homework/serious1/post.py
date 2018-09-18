from mongoengine import Document, StringField, IntField, FloatField

class Post(Document):
    full_name = StringField()
    email = StringField()
    login_name = StringField()
    password = StringField()