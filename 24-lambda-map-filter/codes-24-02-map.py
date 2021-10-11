"""
01/01/2021

Dasturlash asoslari

#24-dars: FUNKSIYALAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
from math import sqrt  # sqrt - kvadrat ildiz

sonlar = list(range(11))  # 0 dan 10 gacha sonlar ro'yxati
# ildizlar = list(map(sqrt,sonlar))
# print(ildizlar)


# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2,sonlar)))

kvadratlar = list(map(lambda x: x * x, sonlar))
# print(kvadratlar)


a = [4, 5, 6]
b = [7, 8, 9]
a_plus_b = list(map(lambda x, y: x + y, a, b))
print(a_plus_b)

# ismlar = ['hasan','husan','olim','umid']
# print(list(map(lambda matn:matn.upper(),ismlar)))
