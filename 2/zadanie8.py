# -*- coding: utf-8 -*-

n = int(input('Podaj n'))
suma = 1

for i in range(1, n+1):
    suma *= i
    
print(suma)