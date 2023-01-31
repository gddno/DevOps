def printing_words(filename):

    try:
	    with open(file_name) as object_file:
		    content = object_file.read()
    except FileNotFoundError:
	    #msg = "Sorry, the file " + file_name + "does not exist."
	    #print(msg)
	    pass
    else:
	    print(content)

file_names = ['./files/cats.txt','./files/dogs.txt']
for file_name in file_names:
    printing_words(file_name)