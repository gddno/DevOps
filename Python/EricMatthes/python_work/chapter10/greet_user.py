import json

file_name = 'nameUser.json'

with open(file_name) as f_obj:
    name = json.load(f_obj)

print("Hi my " + name + "!!!")