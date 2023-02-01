from collections import OrderedDict
favorite_languages = OrderedDict()

favorite_languages['alisa'] = 'python'
favorite_languages['dima'] = 'golang'
favorite_languages['jenya'] = 'c++'
favorite_languages['saha'] = 'java'

for name, language in favorite_languages.items():
    print("\n" + name.title() + "'s favorite language is " + language.title() + ".")




#favorite_languages = {
#	'Alisa' : ['Python', 'C++'],
#	'Dima' : ['Go', 'Python', 'QML'],
#	'Sasha' : ['JavaScript'],
#	'Lena' : ['Java', 'TypeScript']
#	}
#for name, languages in favorite_languages.items():
#	if len(languages) > 1:
#		print("\n" + name.title() + "'s favorite language are:")
#		for language in languages:
#			print("\t" + language.title())
#	else:
#		print("\n" + name.title() + " favorite language is:")
#		for language in languages:
#			print("\t" + language.title())
	
