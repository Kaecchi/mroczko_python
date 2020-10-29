# -*- coding: utf-8 -*-

i = int(input('Podaj i'))
j = int(input('Podaj j'))

print(i, j)

if i ** j > j ** i:
    print(i ** j, " większe")
elif j ** i > i ** j:
    print(j ** i, " większe")
else:
    print("Są równe")
