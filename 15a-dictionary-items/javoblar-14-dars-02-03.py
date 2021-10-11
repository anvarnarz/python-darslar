"""
04/12/2020

Dasturlash asoslari

#15-dars: LUG'AT BILAN ISHLASH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
davlatlar = {
    "o'zbekiston": "toshkent",
    "aqsh": "washington d.c.",
    "rossiya": "moskva",
    "tojikiston": "dushanbe",
    "qirg'iziston": "bishkek",
    "qozog'iston": "nursulton",
    "malayziya": "kuala-lumpur",
    "singapur": "sungapur",
    "italiya": "rim",
}

print("Dunyo davlatlari:")
for davlat in sorted(davlatlar):
    print(davlat.upper())

print("\nDavlatlarning poytaxtlari")
for poytaxt in sorted(davlatlar.values()):
    print(poytaxt.title())

country = input("Qaysi davlatning poytaxtini bilishni istaysiz?:").lower()
capital = davlatlar.get(country)
if capital == None:
    print("Kechirasiz, bizda bu haqida ma'lumot yo'q")
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")
