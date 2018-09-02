person = {
    "name": "Quan",
    "age": 20,
    "city": "Hanoi"
}

for k in person.keys(): #in person
    print(k)

for v in person.values():
    print(v)

for k,v in person.items():
    print(k, v)
    
# print(person)
# print(person["city"])
# person["city"] = "Danang"
# print(person)

# key = "city"
# print(person[key])

# print(person["status"])

# person["status"] = 'complicated'
# print(person)
# del(person["age"])
# print(person)