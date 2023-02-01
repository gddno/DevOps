
enemy = {
    'loc_x': 70,
    'loc_y': 50,
    'color': 'green',
    'health': 100,
    'name': 'Mudillo',
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg'],
    'awards': ['Za Stalina', 'Za Lenina'] 
}

all_enemys = []

for x in range(0, 10):
    all_enemys.append(enemy.copy())
for ene in all_enemys:
    print(ene)

print("-----------------------")

all_enemys[5]['health'] = 30
all_enemys[9]['name'] = 'XXXX'
all_enemys[2]['loc_x'] += 20
for ene in all_enemys:
    print(ene)
    

# print(enemy)

# print("Location X = " + str(enemy['loc_x']))
# print("Location Y = " + str(enemy['loc_y']))
# print("His name is : " + enemy['name'])

# enemy['rank'] = 'Admiral'

# print(enemy)

# del enemy ['rank']

# print(enemy)

# enemy['loc_x'] = enemy['loc_x'] + 40
# enemy['health'] = enemy['health'] - 30
# if enemy['health'] < 80:
#     enemy['color'] = 'yellow'

# print (enemy)

# print(enemy.keys())
# print(enemy.values())