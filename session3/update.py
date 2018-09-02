fav_items = ["video game", "movie", "comic"]
size = len(fav_items)
for i in range(size):
    print(i + 1,". ", fav_items[i], sep="")
print("*" * 10)
p = int(input("Position you want to update? "))
new = input("Your replacing favorite? ")
print("*" * 10)
fav_items[p - 1] = new
for i in range(size):
    print(i + 1,". ", fav_items[i], sep="")