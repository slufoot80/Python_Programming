favorite_languages = {
    'jen': ['python','ruby','php'],
    'sarah': ['C++','java','objective-c'],
    'edward': ['r','perl','javaScript'],
    'phil': ['fortran','sql','pascal'],
}

for name, languages in favorite_languages.items():
    print("\n" + name.title() + "'s favorite languages are:")
    for language in languages:
        print("\t" + language.title())
