"""
25/11/2020

Dasturlash asoslari

#11-dars: if-elif-else

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

mahsulotlar = [
    "un",
    "yog'",
    "sovun",
    "tuxum",
    "piyoz",
    "kartoshka",
    "olma",
    "banan",
    "uzum",
    "qovun",
]

savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

if savat:
    for mahsulot in savat:
        if mahsulot in mahsulotlar:
            print(f"Do'konimizda {mahsulot} bor")
        else:
            print(f"Do'konimizda {mahsulot} yo'q")
else:
    print("Savatingiz bo'sh")
