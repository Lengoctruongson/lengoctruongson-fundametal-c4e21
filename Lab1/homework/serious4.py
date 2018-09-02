from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

customers = db["customers"]

event = {}

customers_list = customers.find()
for i in customers_list:
    n = i['ref']
    if  n not in event:
        event[n] = 1
    else:
        event[n] += 1

print(event)

from matplotlib import pyplot
counts = event.values()
names = event.keys()
pyplot.pie(counts, labels=names, autopct="%.1f%%", shadow=True, explode=[0,0.1,0,0])
pyplot.title("marketing database")
pyplot.axis("equal")
pyplot.show()