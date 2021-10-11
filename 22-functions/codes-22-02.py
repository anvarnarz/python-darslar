"""
24/12/2020

Dasturlash asoslari

#22-dars: *args va **kwargs

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def summa(*sonlar):
    """Kiritilgan sonlar yig'indisini hisoblaydigan funksiya"""
    return sum(sonlar)


print(summa(2))
print(summa(1, 2, 3, 4, 5))
print(summa(4, 5, 6, 7))
