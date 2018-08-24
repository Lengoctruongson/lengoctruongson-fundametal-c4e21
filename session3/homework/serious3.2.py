from random import choice

list_words =["champion", "meticulous", "hexagon"]
for j in range(3):
    w = choice(list_words)
    w1 = list(w)
    for i in range(len(w1)):
        r = choice(w1)
        print(r, end=" ")
        w1.remove(r)
    print()
    a = input("Your answer: ")
    if a == w:
        print("Hura")
    else:
        print(":(")
    list_words.remove(w)
    

