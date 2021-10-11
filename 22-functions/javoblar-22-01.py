"""
24/12/2020

Dasturlash asoslari

#22-dars: *args va **kwargs

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def multiply(*sonlar):
    kopaytma = 1
    for son in sonlar:
        kopaytma *= son
    return kopaytma


print(multiply(4, 5, 6))
