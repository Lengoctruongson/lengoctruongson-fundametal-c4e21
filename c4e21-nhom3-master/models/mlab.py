import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds121373.mlab.com:21373/food

host = "ds121373.mlab.com"
port = 21373
db_name = "food"
user_name = "bach"
password = "bach123"


def connect():
    mongoengine.connect(db_name, host=host, port=port, username=user_name, password=password)

def list2json(l):
    import json
    return [json.loads(item.to_json()) for item in l]


def item2json(item):
    import json
    return json.loads(item.to_json())