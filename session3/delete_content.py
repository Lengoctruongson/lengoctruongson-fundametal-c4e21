fav_items = ['sleeping', 'eating', 'rolling', 'jumping']
for index, item in enumerate(fav_items):
    print(index+1, ". ", item, sep="")
print("*" * 30)
p = input("Favorite content you want to get rid of? ")

if p in fav_items:
    fav_items.remove(p)
    for index, item in enumerate(fav_items):
        print(index+1, ". ", item, sep="")
else:
    print("Nah")
print("*" * 30)
