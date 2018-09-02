fav_items = ["video game", "movie", "comic"]
# print(*fav_items, sep=", ")
# new_item = input("What is your new interest? ")
# fav_items.append(new_item)
# print(*fav_items, sep=", ")

# fori
size = len(fav_items)
for i in range(size):
    print(i +1,". ", fav_items[i], sep="")