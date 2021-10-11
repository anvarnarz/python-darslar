"""
01/01/2021

Dasturlash asoslari

#24-dars: FUNKSIYALAR SO'NGSO'Z

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
from random import sample
from math import sqrt

x = list(range(0, 1001))
y = sample(x, k=10)
print(y)

ildizlar = list(map(lambda n: sqrt(n), y))
print(ildizlar)

toq_sonlar = list(filter(lambda n: n % 2, y))
print(toq_sonlar)
