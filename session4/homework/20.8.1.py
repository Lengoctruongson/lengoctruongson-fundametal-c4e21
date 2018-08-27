words = input("Enter data: ")
words_list = list(words)
count = {}
for i in words_list:
    if i != " ":
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
n = sorted(count.items())
for j in n:
    print(*j)
