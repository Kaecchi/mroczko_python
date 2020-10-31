# -*- coding: utf-8 -*-

n = int(input('Podaj n'))
wart = 0

for i in range(2, n-1):
    if n % i == 0:
        wart = 1

if wart == 1:
    print('Złożona')
else:
    print('Pierwsza')