import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds157522.mlab.com:57522/c4e21-blog

host = "ds157522.mlab.com"
port = 57522
db_name = "c4e21-blog"
user_name = "Son Le"
password = "leson1871995"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())