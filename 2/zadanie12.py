# -*- coding: utf-8 -*-

wart = 0

print('1')

for i in range(2, 201):
    for j in range(2, i):
        if i % j == 0:
            wart = 1
    if wart == 0:
        print(i)

    wart = 0