"""
18/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def aylana_info(radius, pi=3.14159):
    aylana = {
        "radius": radius,
        "diametr": 2 * radius,
        "perimetr": 2 * radius * pi,
        "yuza": pi * radius ** 2,
    }
    return aylana
