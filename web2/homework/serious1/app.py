from flask import Flask, render_template, request
app = Flask(__name__)
import mlab
from post import Post

mlab.connect()

@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "GET":
        return render_template("register.html")
    elif request.method == "POST":
        form = request.form
        f = form["full_name"]
        e = form["email"]
        l = form["login_name"]
        p = form["password"]
        
        register = Post(full_name=f, email=e, login_name=l, password=p)
        register.save()
        return "OK"
if __name__ == "__main__":
    app.run(debug=True)