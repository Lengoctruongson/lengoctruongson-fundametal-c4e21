sheeps = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Son and these are my sheeps sizes")
print(sheeps)
l = len(sheeps)
print()

biggest_sheep = 0
for i in range(l):
    if sheeps[i] > biggest_sheep:
        biggest_sheep = sheeps[i]
print("My biggest has size", biggest_sheep, "let's shear it")
print("After shearing , here is my flock")
p = sheeps.index(biggest_sheep)
sheeps[p] = 8
print(sheeps)

for q in range(2):
    print("MONTH", q+1, ":")
    print("One month has passed, now here is my flock")
    for j in range(l):
        sheeps[j] = sheeps[j] + 50
    print(sheeps)

    biggest_sheep = 0
    for i in range(l):
        if sheeps[i] > biggest_sheep:
            biggest_sheep = sheeps[i]
    print("My biggest has size", biggest_sheep, "let's shear it")

    print("After shearing , here is my flock")
    p = sheeps.index(biggest_sheep)
    sheeps[p] = 8
    print(sheeps)
    print()

print("MONTH", 3, ":")
print("One month has passed, now here is my flock")
for j in range(l):
    sheeps[j] = sheeps[j] + 50
print(sheeps)
print()
       
total = 0
for q in range(l):
    total = total + sheeps[q]
print("My flock has size in total:", total)
print("I would get ", total, " *$2 = ", total*2, "$", sep="")