# -*- coding: utf-8 -*-

n = int(input('Podaj n'))
suma = 0

for i in range(1, n+1):
    if n % i == 0:
        suma += 1
        print(i)

print(suma)