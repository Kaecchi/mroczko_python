# -*- coding: utf-8 -*-

rok = int(input('Podaj rok'))

print(rok)

if rok % 100 == 0 and rok % 400 == 0:
    print('Przestępny')
elif rok % 100 == 0:
    print('Nieprzestępny')
elif rok % 4 == 0:
    print('Przestępny')
else:
    print('Nieprzestępny')
