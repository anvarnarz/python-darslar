"""
22/12/2020

Dasturlash asoslari

#21-dars: FUNKSIYAGA RO'YXAT UZATISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def katta_harf(matnlar):
    matnlar = matnlar[:]
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()
    return matnlar


ismlar = ["ali", "vali", "hasan", "husan"]
yangi_ismlar = katta_harf(ismlar)
print(ismlar)
print(yangi_ismlar)
