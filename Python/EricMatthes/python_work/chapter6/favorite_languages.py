favorite_languages = {
    'dima':'python',
    'jenya':'c++',
    'danila':'go',
    'iliya':'php',
    'lena':'java',
    'artem':'java'
}
for name, language in sorted(favorite_languages.items()):
    print(f"{name.title()} love is {language.title()}")
print("\n")

freinds = ['lena', 'jenya']
for name in favorite_languages.keys():
    print(name.title())
    if name in freinds:
        language = favorite_languages[name].title()
        print(f"Hi {name.title()} i know your favorite language is {language}")
if 'nikita' not in favorite_languages.keys():
    print(f"Nilita please start study:)")
for language in favorite_languages.values():
    print(language)
print('------------------------')
for language in set(favorite_languages.values()):
    print(language)
