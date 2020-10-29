# -*- coding: utf-8 -*-

i = 2 ** (1/2)
j = 3 ** (1/3)
k = 5 ** (1/5)

print(i, j ,k)

if i > j:
    if i > k:
        print(i, ' największe')
    else:
        print(k, ' największe')
else:
    print(j, ' największe')
