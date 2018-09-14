#1. Creat a flask app
from flask import Flask, render_template

app = Flask(__name__)

ps = [
        "Trong đầm gì đẹp bằng sen aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
        "Lá xanh bông trắng lại chen nhị vàngbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbbb",
        "Nhị vàng bông trắng lá xanh ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc"
    ]

#2. Creat router
@app.route("/")
def homepage():
   
    return render_template("homepage.html",
    title="Ca dao về sen",
    posts=ps)

@app.route("/huy")
def huypage():
    return "Hello Huy"

@app.route("/hello/<name>")
def hello(name):
    return "Hello " + name

@app.route("/posts/<int:position>")
def post_detail(position):
    if position < 0 or position >= len(ps):
        return "Not found", 404
    post = ps[position - 1]
    return render_template("post_detail.html", post=post)

@app.route("/posts")
def posts():
    shortened_ps = []
    for post in ps:
        shortened_ps.append(post[0:20])
    return render_template("post_list.html", posts=shortened_ps)

# @app.route("/add/<number1>/<number2>")
# def add(number1,number2):
#     add = str(int(number1) + int(number2))
#     return add

@app.route("/add/<int:a>/<int:b>")
def add(a,b):
    result = a+b
    return str(result)

@app.route("/h1tag")
def h1tag():
    return "<h1>Heading 1 - Bigggg</h1><p>Hom nay toi buon</p>"

#3. Run app
print("Running app")
if __name__ == "__main__":
    app.run(debug=True) # listening