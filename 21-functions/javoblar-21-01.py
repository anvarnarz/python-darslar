"""
22/12/2020

Dasturlash asoslari

#21-dars: FUNKSIYAGA RO'YXAT UZATISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def katta_harf(matnlar):
    for i in range(len(matnlar)):
        matnlar[i] = matnlar[i].title()


ismlar = ["ali", "vali", "hasan", "husan"]
katta_harf(ismlar)
print(ismlar)
