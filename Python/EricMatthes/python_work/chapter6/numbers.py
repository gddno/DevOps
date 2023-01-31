number = {
    'Bill' : 1,
    'Marry' : 45,
    'Dima' : 0,
    'Masha' : 123,
    'Vadim' : 5
}
for key, value in number.items():
    print(f"\n{key}:{value}")

glossary = {
    'dima':'zhuravlev',
    'katya':'smirnova',
    'genia':'korobeinikov',
    'iliya':'sharkov',
    'katia':'zhuravleva',
    'oksana':'smirnova'
}
for last_name in set(glossary.values()):
    print(last_name)
