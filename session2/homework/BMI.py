h = int(input("How high are you (cm)? "))
w = int(input("What is your weight (kg) "))
h1 = h / 100
BMI = w / h1
if BMI < 16:
    print("You are severely underweight")
elif 16 <= BMI < 18.5:
        print("You are underweight")
elif 185 <= BMI < 25:
    print("You are normal")
elif 25 <= BMI < 30:
    print("You are overweight")
else:
    print("You are obese")