aliens = []

for aline in range(30):
    new_aline = {'color': 'green', 'points': 5, 'speed':'slow'}
    aliens.append(new_aline)
for aline in aliens[0:3]:
    if aline['color'] == 'green':
        aline['color'] = 'yellow'
        aline['points'] = 10
        aline['speed'] = 'medium'
for aline in aliens[0:1]:
    if aline['color'] == 'yellow':
        aline['color'] = 'red'
        aline['points'] = 15
        aline['speed'] = 'fast'
for aline in aliens[:5]:
    print(aline)
print("......")
print(f"Total counter aliens: {len(aliens)}")