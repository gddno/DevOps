import re

input_filename = "../SuportFiles/dumpfile.txt"
result_filename = "../SuportFiles/Results.txt"

inputfile = open(input_filename, mode = "r", encoding="Latin-1")
resultfile = open(result_filename, mode = "w", encoding="Latin-1")

mytext = inputfile.read()

lookfor = r"[\w.-]+@(?!inbox\.ru)[A-Za-z]+\.[\w.]+"

results = re.findall(lookfor, mytext)

for item in results:
    print(item)
    resultfile.write(item + "\n")

print("Total is: " + str(len(results)))