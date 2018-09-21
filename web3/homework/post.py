from mongoengine import Document, StringField

class Post(Document):
    title = StringField()
    author = StringField()
    content = StringField()
    