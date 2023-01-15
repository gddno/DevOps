def formatte_name(first, last, midle = ''):
    if midle:
	    full_name = first + ' ' + midle + ' '  + last
    else:
	    full_name = first + ' ' + last
    return full_name.title()
musician = formatte_name('dima', 'zhuravlev')
print(musician)
musician = formatte_name(first = 'dima', midle = 'krasavchik',last = 'zhuravlev')
print(musician)