def get_param(country, city, count=''):
	if count:
		string = f"{country} {city} {count}"
	else:
		string = f"{country} {city}"
	return string.title()