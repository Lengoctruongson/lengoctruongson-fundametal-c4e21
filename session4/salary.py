from collections import OrderedDict

r1 = {
    "#": 1,
    "name": "Son",
    "level": 25,
    "hour": 4,
}
r2 = {
    "#": 2,
    "name": "Trung",
    "level": 20,
    "hour": 7,
}
r3 = {
    "#": 3,
    "name": "Chi",
    "level": 15,
    "hour": 4,
}

salary_list = [r1, r2, r3]
total_wage = 0
wage_list = []
for salary in salary_list:
    name = salary["name"]
    # print(salary["hour"])
    hour = salary["hour"]
    level = salary["level"]
    wage = hour * level
    total_wage += wage
    new = OrderedDict({
        "name": name,
        "salary": wage,
        "hour": hour,
    })
    wage_list.append(new)
    print(name, "'s wage: ", wage)
print("Total wage: ", total_wage)
for i in wage_list:
    print(i)

import pyexcel
pyexcel.save_as(records=wage_list, dest_file_name="wage_output.xlsx")

# print(salary_list)

# for x in salary_list:
#     print(x)