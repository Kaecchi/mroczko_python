# -*- coding: utf-8 -*-

i = float(input('Podaj i'))
j = float(input('Podaj j'))

print(i, j)

i2 = i - (i % 1) + (j % 1)
j2 = j - (j % 1) + (i % 1)

print(i2, j2)

print(i2, j2)

# dla i = 12.34, j = 65.87 dziwne wyniki
# dla i = 12.34, j = 65.43 dziwne wyniki
