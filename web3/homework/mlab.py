import mongoengine

#mongodb://<dbuser>:<dbpassword>@ds211083.mlab.com:11083/web3_homework

host = "ds211083.mlab.com"
port = 11083
db_name = "web3_homework"
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