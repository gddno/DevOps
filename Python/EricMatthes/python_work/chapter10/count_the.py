file_path = './files/LordLister.txt'
with open(file_path) as object_file:
    content = object_file.read()
    print(content.lower().count('the'))
