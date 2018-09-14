from flask import Flask, render_template

serious2 = Flask(__name__)
users = {
    "son": {
        "name": "Le Ngoc Truong Son",
        "age": "23",
        "hobbies": "swimming"
    },
    "trung": {
        "name": "Le Trung",
        "age": "19",
        "hobbies": "jumping"
    }
}

@serious2.route("/user/<username>")
def tada(username):
    if username in users:
        return render_template("user.html", posts=users[username])
    else:
        return "User not found"

if __name__ == "__main__":
    serious2.run(debug=True)