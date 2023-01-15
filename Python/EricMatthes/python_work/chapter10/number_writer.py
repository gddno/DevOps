import json

file_name = 'test2.json'
numbers = [23,423,4234,242,656,76,76,523,0,434,45]

with open(file_name, 'w') as f_obj:
    json.dump(numbers, f_obj)