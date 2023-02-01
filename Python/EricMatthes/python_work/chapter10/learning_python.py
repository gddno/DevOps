path_to_file = './files/learning_python.txt'

with open(path_to_file) as file_object:
    content = file_object.read()
    print(content)
print('------------------------------------------------')
with open(path_to_file) as file_object:
    for line in file_object:
	    print(line)

print('------------------------------------------------')
with open(path_to_file) as file_object:
    lines = file_object.readlines()
for line in lines:
	print(line.strip().replace('Python', 'C'))
print('------------------------------------------------')
a = ''
for line in lines:
    a += line.rstrip()
print(a)
