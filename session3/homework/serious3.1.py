from random import choice
words = ['c', 'h', 'a', 'm', 'p', 'i', 'o', 'n']
for i in range(8):
    r = choice(words)
    print(r, end=" ")
    words.remove(r)
print()
a = input("Your answer: ")
if a == "champion":
    print("Hura")
else:
    print(":(")