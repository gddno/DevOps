file_path = './files/test_write.txt'

with open(file_path, 'w') as file_object:
    file_object.write("Hi everyone\n")
    file_object.write("Hi Dima\n")
with open(file_path, 'a') as file_object:
    file_object.write('And I add new line\n')
    file_object.write('And you hear me\n')