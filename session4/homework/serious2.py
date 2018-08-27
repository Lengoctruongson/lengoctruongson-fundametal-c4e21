price = {
    "banana": 4,
    "apple": 2,
    "orange": 1.5,
    "pear": 3,
}

stock = {
    "banana": 6,
    "apple": 0,
    "orange": 32,
    "pear": 15,
}

total = 0

for k,v in price.items():
    print(k)
    print("price:", v)
    print("stock:", stock[k])
    each_fruit = v * stock[k]
    total += each_fruit
    print()
print("Your money:", total)