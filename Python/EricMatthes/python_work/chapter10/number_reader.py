import json

file_name = 'test.json'
with open(file_name) as f_obj:
    numbers = json.load(f_obj)
print(numbers)