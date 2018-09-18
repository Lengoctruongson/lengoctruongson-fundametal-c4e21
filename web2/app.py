from flask import Flask, render_template, request
app = Flask(__name__)
import mlab
from post import Post

mlab.connect()

p = {
    "title": "C4E21",
    "content": "Module web, sắp hackathon",
    "author": "Quân",
    "date": "2018/09/02",
}

ps = [
{
    "title": "C4E21",
    "content": "Module web, sắp hackathon",
    "author": "Quân",
    "date": "2018/09/02",
},
{
    "title": "C4E21 - Hackathon",
    "content": "8 giờ code, hoàn thiện sản phẩm",
    "author": "Huy",
    "date": "2019/03/03",
},
{
    "title": "Learning",
    "content": "Coding",
    "author": "Sơn",
    "date": "2018/09/15",
}
]

@app.route("/post")
def post():
    return render_template("dict.html", post=p)

@app.route("/posts")
def posts():
    return render_template("dicts.html", posts=ps)

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        #1. Get form & extract data
        form = request.form
        t = form["title"]
        a = form["author"]
        c = form["content"]
        
        #2. Add new post
        new_post = Post(title=t, author=a, content=c, likes=0)
        new_post.save()

        return "OK"
if __name__ == "__main__":
    app.run(debug=True)