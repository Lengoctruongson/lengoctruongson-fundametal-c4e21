fav_items = ['sleeping', 'eating', 'rolling', 'jumping']
for index, item in enumerate(fav_items):
    print(index+1, ". ", item, sep="")
print("*" * 30)
p = int(input("Favorite position you want to get rid of? "))
fav_items.pop(p - 1)
print("*" * 30)
for index, item in enumerate(fav_items):
    print(index+1, ". ", item, sep="")