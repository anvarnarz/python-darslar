"""
01/01/2021

Dasturlash asoslari

#24-dars: FUNKSIYALAR SO'NGSO'Z

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import math

# def nom(argument):
# return ifoda

# uzunlik = lambda pi, r : 2*pi*r
# print(uzunlik(math.pi,10))

# kvadrat = lambda x, y : x ** y
# print(kvadrat(3, 2))


def daraja(n):
    return lambda x: x ** n


kvadrat = daraja(2)
kub = daraja(3)
print(f"3-ning kvadrati {kvadrat(3)} ga, " f"kubi {kub(3)} ga teng")
