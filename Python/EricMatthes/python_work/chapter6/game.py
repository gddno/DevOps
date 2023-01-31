aline_0 = {'x_position':0, 'y_position':25, 'speed':'medium'}
aline_0['speed'] = 'fast'
print(f"Original position: {aline_0['x_position']}")
if aline_0['speed'] == 'slow':
    x_increment = 1
elif aline_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
aline_0['x_position'] = aline_0['x_position'] + x_increment

print(f"Currently position: {aline_0['x_position']}")

