from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
import mlab
from post import Post

mlab.connect()

@app.route("/post_detail/<post_id>")
def post_detail(post_id):
    post = Post.objects().with_id(post_id)
    return render_template("post_detail.html", post=post)

@app.route("/posts")
def posts():
    all_posts = Post.objects()
    return render_template("posts.html", posts = all_posts)

@app.route("/delete/<post_id>")
def delete(post_id):
    post = Post.objects().with_id(post_id)
    post.delete()
    return redirect(url_for("posts"))

@app.route("/update/<post_id>", methods = ['GET', 'POST'])
def update(post_id):
    post = Post.objects().with_id(post_id)
    if request.method == 'GET':
        return render_template('update.html', post = post)
    elif request.method == 'POST':
        form = request.form
        t = form['title']
        a = form['author']
        c = form['content']
        post.update(set__title=t, set__author=a, set__content=c)
        return redirect(url_for("posts"))

@app.route("/new_post", methods=["GET", "POST"])
def new_post():
    if request.method == "GET":
        return render_template("new_post.html")
    elif request.method == "POST":
        form = request.form
        t = form["title"]
        a = form ["author"]
        c = form["content"]

        new_post = Post(title=t, author=a, content=c)
        new_post.save()

        return redirect(url_for("posts"))

if __name__ == "__main__":
    app.run(debug=True)