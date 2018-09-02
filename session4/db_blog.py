# 1. Connect to database
from pymongo import MongoClient
from bson.objectid import ObjectId
uri = "mongodb://admin:toilason69@ds135852.mlab.com:35852/c4e"

client = MongoClient(uri)
db = client.get_default_database()

# 2. Sellect collection
posts = db["post"]

# 3. Creat document
post = {
    "title": "thi thoang di choi",
    "content": "hihi, haha",
    "random": "nhay nhot"
}

# 4. Insert document
# posts.insert_one(post)
# print("Done")

post_list = posts.find()
# for post in post_list: # post_list ~ collection ~list
#     print(post['content']) # post ~ document ~ dictionary
cond = {
    "title": {
        "$regex": "hom nay",
        "$options": "i",
    }
}
post = posts.find_one(cond)
print(post)