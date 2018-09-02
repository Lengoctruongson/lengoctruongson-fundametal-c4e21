items = [4, 6, 56, -8, 1, 90, -43]
x = int(input("Enter a number: "))

if x in items:
    print("Found")
    found_index = items.index(x)
    print(found_index)
else:
    print("Not found")