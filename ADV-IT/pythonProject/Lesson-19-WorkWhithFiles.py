
inputfile = "../SuportFiles/user_name.txt"
inputfile2 = "../SuportFiles/list_of_password.txt"
outputfile = "../SuportFiles/mypasswords.txt"

password_tolookfor = "j"

myfile1 = open(inputfile, mode = 'r', encoding = 'latin_1')
myfile2 = open(inputfile2, mode = 'r', encoding= 'latin_1')
myfile3 = open(outputfile, mode = 'a', encoding= 'latin_1')
#print(myfile.read())

for num, line in enumerate(myfile1, 1):
 if "Zhuravlev" in line:
  print(str(num) + " Hello " + line.strip())

for num, line in enumerate(myfile2, 1):
 if password_tolookfor in line:
  print(str(num) + " " + line.strip())
  myfile3.write("Found password: " + line)

myfile1.close()
myfile2.close()
myfile3.close()