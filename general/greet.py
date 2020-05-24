def greet(lang):
    if(lang == 'es'):
        print('Hola')
    elif(lang == 'fr'):
        print('Bonjour')
    elif(lang == 'hn'):
        print('Namaste')
    else:
        print('hello')

name = input('Enter your name\n')
lang = input('Enter your language\n')
print(greet(lang),name)
