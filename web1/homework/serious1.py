from flask import Flask, render_template

serious1 = Flask(__name__)

@serious1.route("/bmi/<int:weight>/<int:height>")
def bmi(weight, height):
    bmi = weight / (height/100)**2
    a = ""
    if bmi< 16:
        a = 'Severely underweight'
    elif 16 <= bmi < 18.5:
        a = 'Underweight'
    elif 18.5 <= bmi < 25:
        a = 'Normal'
    elif 25 <= bmi < 30:
        a = 'Overweight'
    else:
        a = 'Obese'
    # return "<p>BMI = {0}<p><p>Condition: {1}<p>".format(bmi, a)
    return render_template("bmi.html", bmi=bmi, a=a)

if __name__ == "__main__":
    serious1.run(debug=True)