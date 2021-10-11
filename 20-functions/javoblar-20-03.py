"""
18/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def kattasi(x, y, z):
    max = x
    if y >= max:
        max = y
    if z >= max:
        max = z
    return max
