from pymongo import MongoClient

uri = "mongodb://admin:admin@ds021182.mlab.com:21182/c4e"

client = MongoClient(uri)
db = client.get_default_database()

posts = db["post"]

post = {
    "title": "Hi everyone",
    "author": "Le Ngoc Truong Son",
    "content": "C4E21 are awesome. Stay focus in class, do your home work and have some fun",
}

posts.insert_one(post)
print("Done")