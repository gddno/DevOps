import json

numbers = [1,3,34,545,43,435,23,4,34,324]
file_name = 'test.json'

with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)