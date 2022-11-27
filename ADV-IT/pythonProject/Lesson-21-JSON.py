import json

filename = "../SuportFiles/user_settings.txt"
myfile = open(filename, mode = 'w', encoding= 'Latin-1')
player1 = {
    'PlayerName': 'Donal Trump',
    'Score': 345,
    'awards': ["OR", "NV", "NY"]
}

player2 = {
    'PlayerName': 'Clinton Hillary',
    'Score': 346,
    'awards': ["MY", "TO", "OC", "FI"]
}

myplayers = []
myplayers.append(player1)
myplayers.append(player2)

#-------------Save by JSON-----------------

json.dump(myplayers, myfile)
myfile.close()

# -------Load by JSON----------

myfile = open(filename, mode='r', encoding="Latin-1")
json_date = json.load(myfile)

for user in json_date:
    print("Player Name is : " + str(user['PlayerName']))
    print("Score is: " + str(user['Score']))
    print("Player Awards N1: "+ str(user['awards'][0]))
    print("player Awards N2: "+ str(user['awards'][1]))
    print("Player Awards N3: " + str(user['awards'][2]))
    print("---------------------\n\n")