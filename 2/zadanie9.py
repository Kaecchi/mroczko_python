# -*- coding: utf-8 -*-

n = int(input('Podaj n'))
m = int(input('Podaj m'))
suma = 1

for i in range(1, m+1):
    suma *= n

print(suma)