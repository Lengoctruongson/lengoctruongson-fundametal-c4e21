favs = ['netflix', 'teaching', 'redbull']
for i, item in enumerate(favs):
    print(i+1,item)

while True:
    command = input("What do you want (C, R, U, D)? ").upper()
    if command == "C":
        a = input("What do you want to add? ")
        favs.append(a)
        for i, item in enumerate(favs):
            print(i+1,item)
    elif command == "R":
        for i, item in enumerate(favs):
            print(i+1,item)
    elif command == "U":
        p = int(input("Position you want to update? "))
        c = input("Replaceing item? ")
        favs[p-1] = c
        for i, item in enumerate(favs):
            print(i+1,item)
    elif command == "D":
        p1 = int(input("Position you want to delete? "))
        favs.pop(p1-1)
        for i, item in enumerate(favs):
            print(i+1,item)
    else:
        print("Nah")