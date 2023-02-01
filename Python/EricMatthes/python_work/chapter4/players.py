players = ['martin', 'loodvig', 'julia', 'anna', 'dmitrii']
new_plaeyrs = players[:]
#player = [value for value in players[0:3]]
#print(player)
print("This is the best plaers:")
for plaer in players[-3:]:
    print(plaer)

print(players)
print(new_plaeyrs)
players.append('iliya')
new_plaeyrs.append('luba')
print(players)
print(new_plaeyrs)