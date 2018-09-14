
from flask import Flask, render_template, redirect
exercise1 = Flask(__name__)

@exercise1.route("/about-me")
def about_me():
    return render_template("about_me.html")

@exercise1.route("/school")
def school():
    return redirect("http://techkids.vn/")

if __name__ == "__main__":
    exercise1.run(debug=True)