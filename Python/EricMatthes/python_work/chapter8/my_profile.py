def build_profile(first, last, **my_profile):
    profile = {}
    profile['first_name'] = first
    profile['last_name'] = last
    for key, value in my_profile.items():
	    profile[key] = value
    return profile
dima_profile = build_profile('zhuravlev', 'dima', hobbi = 'footboal', country = 'russia', city = 'krasnodar')
print(dima_profile)
