from flask import Flask, render_template, request, redirect, url_for
from models import mlab
from models.food import Food
mlab.connect()
app = Flask(__name__)

@app.route("/")
def home():
    # all_home = home.objects()
    # return render_template("home.html", home=all_home)
    return render_template("home.html")
@app.route("/capdoi")
def capdoi():
    foods = Food.objects(chu_de = "couple")
    return render_template("capdoi.html", foods = foods)


@app.route("/cap_doi/<food_id>")
def cap_doi(food_id):
    food = Food.objects().with_id(food_id)
    return render_template("cap_doi.html", food = food)
@app.route("/giadinh")
def giadinh():
    foods = Food.objects(chu_de = "family")
    return render_template("giadinh.html", foods = foods)
@app.route("/gia_dinh/<food_id>")
def gia_dinh(food_id):
    food = Food.objects().with_id(food_id)
    return render_template("gia_dinh.html", food = food)
@app.route("/ngayle")
def ngayle():
    foods = Food.objects(chu_de = "ngayle")
    return render_template("ngayle.html", foods = foods)
@app.route("/ngay_le/<food_id>")
def ngay_le(food_id):
    food = Food.objects().with_id(food_id)
    return render_template("ngay_le.html", food = food)
if __name__ == "__main__":
    app.run(debug=True)