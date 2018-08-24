clothes = ['T-shirt', 'Sweater']

while True:
    n = input("Welcome to out shop, what do you want (C, R, U, D)? ")
    if n == "C":
        new = input("Enter new item: ")
        clothes.append(new)
        print("Our item: ", end="")
        print(*clothes, sep=", ")
    elif n == "R":
        print("Our item: ", end="")
        print(*clothes, sep=", ")
    elif n == "U":
        p = int(input("Update position: "))
        update = input("New item? ")
        clothes[p-1] = update
        print("Our item: ", end="")
        print(*clothes, sep=", ")
    elif n == "D":
        p1 = int(input("Delete position? "))
        clothes.pop(p1-1)
        print("Our item: ", end="")
        print(*clothes, sep=", ")
    else:
        print("Nah")