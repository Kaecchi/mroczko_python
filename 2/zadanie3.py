# -*- coding: utf-8 -*-

m, n = input('Podaj m i n po przecinku').split(',')

if int(m) <= int(n):
    for i in range(int(m), int(n)+1):
        print(i, end = " ")
elif int(m) > int(n):
    for i in range(int(m), int(n)+1, -1):
        print(i, end = " ")
