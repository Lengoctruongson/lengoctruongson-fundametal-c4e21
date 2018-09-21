import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds261072.mlab.com:61072/web2_homework

host = "ds261072.mlab.com"
port = 61072
db_name = "web2_homework"
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