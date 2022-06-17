#Password Validation Tool by rene.jock@outlook.de
import re

upper_letter = 'ABCDEFGHIJKLMNOPSTUVWXYZ'
lower_letter = upper_letter.lower()
digits = '1234567890'
symbols = '_.,:@%!?()'
minChar = 8

print('Willkommen beim Password Validation Tool')

def validation():
    while True:
        pwd = input('Bitte gebe das zu überprüfende Password ein : ')

        if len(pwd) < minChar:
            print('+ Dein Passwort ist kleiner als 8 Zeichen.')
        elif re.search('[0-9]', pwd) is None:
            print('+ Ein sicheres Passwort sollte mindestens eine Zahl von 0 - 9 enthalten.')
        elif re.search('[A-Z]', pwd) is None:
            print('+ Dein Passwort sollte mindesten 1 Großbuchstaben enthalten.')
        elif re.search('[a-z]', pwd) is None:
            print('+ Dein Passwort sollte mindesten 1 kleinen buchstaben enthalten.')
        else:
            print('Super, dein Passwort ist nun sicher!')
            break

validation()