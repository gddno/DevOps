def build_car_profile(marka, model, **toppings):
    profile = {}
    profile['marka'] = marka
    profile['model'] = model
    for key, value in toppings.items():
	    profile[key] = value
    return profile

car_profile = build_car_profile('BMW', 'M5', color = 'black', status = 'new')
print(car_profile)