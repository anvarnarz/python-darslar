"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

buxoriy = {
    "ism": "Abu Abdulloh Muhammad ibn Ismoil",
    "tyil": 810,
    "vyil": 870,
    "tjoy": "Buxoro",
}

qodiriy = {"ism": "Abdulla Qodiriy", "tyil": 1894, "vyil": 1938, "tjoy": "Toshkent"}

vohidov = {"ism": "Erkin Vohidov", "tyil": 1936, "vyil": 2016, "tjoy": "Farg'ona"}

navoiy = {"ism": "Alisher Navoiy", "tyil": 1441, "vyil": 1501, "tjoy": "Xirot"}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    tyil = shaxs["tyil"]
    vyil = shaxs["vyil"]
    tjoy = shaxs["tjoy"]
    print(
        f"{ism} {tyil}-yilda {tjoy}da tavallud topgan. " f"{vyil-tyil} yil umr ko'rgan."
    )
