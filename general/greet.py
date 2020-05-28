# Program to greet user
# Function definition
def greet(lang):
    if(lang == 'es'):
        print('Hola')
    elif(lang == 'fr'):
        print('Bonjour')
    elif(lang == 'hn'):
        print('Namaste')
    else:
        print('hello')
# Taking input from user
name = input('Enter your name\n')
lang = input('Enter your language\n')
# Invoking Function
print(greet(lang),name)
