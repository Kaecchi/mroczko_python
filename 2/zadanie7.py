# -*- coding: utf-8 -*-

n = int(input('Podaj n'))
m = 0
wart = 0

while(m < n):
    m += 1
    if n == m*m:
        print('n to kwadrat', m)
        wart = 1

if wart == 0:
    print('n nie jest kwadratem')