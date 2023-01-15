with open('./files/pi_digits.txt') as file_object:
    lines = file_object.readlines()
pi_string = ''
for line in lines:
    pi_string += line.strip()
birthday = input("Enter your birthday, in the form ddmmyy: ")
if birthday in pi_string:
    print("\nYour birthday appears in first million digits of pi!!!")
else:
    print("\nYour birthday don't appers in first million digits of pi!!!")
#print(pi_string[:12]+"...")
#print(len(pi_string))