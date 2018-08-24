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
print()

print("After shearing , here is my flock")
p = sheeps.index(biggest_sheep)
sheeps[p] = 8
print(sheeps)