promt = "\n Please tell me something and I repeat you)"
promt += "\nEntet your word and if it wiil quit my programm end!!!"

message = ""
while message !='quit':
    message = input(promt)

    if message != 'quit':
	    print(message) 