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
    "asarlar": [
        "Al-jome’ as-sahih",
        "Al-adab al-mufrad",
        "At-tarix al-kabir",
        "At-tarix as-sag‘ir",
    ],
}

qodiriy = {
    "ism": "Abdulla Qodiriy",
    "tyil": 1894,
    "vyil": 1938,
    "tjoy": "Toshkent",
    "asarlar": ["O'tkan kunlar", "Mehrobdan Chayon", "Obid ketmon"],
}

vohidov = {
    "ism": "Erkin Vohidov",
    "tyil": 1936,
    "vyil": 2016,
    "tjoy": "Farg'ona",
    "asarlar": ["Tong nafasi", "Qo'shiqlarim sizga", "O'zbegim", "Qiziquvchan Matmusa"],
}

navoiy = {
    "ism": "Alisher Navoiy",
    "tyil": 1441,
    "vyil": 1501,
    "tjoy": "Xirot",
    "asarlar": ["Xamsa", "Lison ut-Tayr", "Mahbub Al-Qulub", "Munojot"],
}

shaxslar = [buxoriy, qodiriy, vohidov, navoiy]

for shaxs in shaxslar:
    ism = shaxs["ism"]
    asarlar = shaxs["asarlar"]
    print(f"\n{ism} ning mashxur asarlari: ")
    for asar in asarlar:
        print(asar)
