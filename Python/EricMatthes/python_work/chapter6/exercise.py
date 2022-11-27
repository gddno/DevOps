ronaldo = {'hight':189, 'widht':78, 'contry':'portugal', 'color':'red'}
print(ronaldo['hight'])
print(ronaldo['widht'])
print(ronaldo['contry'])
print(ronaldo['color'])

glossary = {
    'list':'1',
    'kortag':'2',
    'glossary':'3',
    'variable':'4'
}
for word in glossary:
    print(f"This key: {word} and this value: {glossary[word]}")