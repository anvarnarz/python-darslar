"""
17/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def oraliq(min, max):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += 1
    return sonlar


print(oraliq(0, 10))
print(oraliq(10, 21))

# def oraliq(min,max,qadam=1):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar

# print(oraliq(0,21,2))
