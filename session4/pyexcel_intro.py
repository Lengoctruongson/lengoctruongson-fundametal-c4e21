import pyexcel

# 1. Prepare data

data = [
    {
        "name": "Son",
        "age": 23,
    },
    {
        "name": "Trung",
        "age": 19,
    },
    {
        "name": "Dung",
        "age": 21,
    },
]

# 2. Save
pyexcel.save_as(records=data, dest_file_name="sample.xlsx" )