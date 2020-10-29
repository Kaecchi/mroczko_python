# -*- coding: utf-8 -*-

i = int(input('Podaj i'))
j = int(input('Podaj j'))
k = int(input('Podaj k'))

napis = ''

if i > 10:
    napis += str(i) + ' '
if j > 10:
    napis += str(j) + ' '
if k > 10:
    napis += str(k) + ' '
    
print(napis)
