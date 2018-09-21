from flask import Flask, render_template, request, redirect, url_for
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

@app.route("/post/<post_id>")
def post(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("post_detail.html", post=post)

@app.route("/posts")
def posts():
    all_posts = Post.objects()
    return render_template("posts.html", posts=all_posts)

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

        return redirect(url_for("posts"))

@app.route("/delete/<post_id>")
def delete(post_id):
    post = Post.objects().with_id(post_id)
    if post is None:
        print("Post not found")
    else:
        post.delete()
        return redirect(url_for("posts"))

@app.route("/update/<post_id>")
def update(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("update_post.html", post=p)
# làm nốt submit author

if __name__ == "__main__":
    app.run(debug=True)