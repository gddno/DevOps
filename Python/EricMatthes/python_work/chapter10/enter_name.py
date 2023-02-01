path_to_file = './files/test_write.txt'
name = input("Please enter your name: ")

with open(path_to_file, 'a') as file_object:
    file_object.write(name + '.\n')