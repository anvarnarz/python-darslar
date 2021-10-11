"""
16/12/2020

Dasturlash asoslari

#19-dars: FUNCTIONS (FUNKSIYALAR)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# Foydalanuvchidan son qabul qilib, sonni 2, 3, 4 va 5 ga qoldiqsiz bo'linishini tekshiruvchi
# funksiya yozing.
# Natijalarni konsolga chiqaring ("15 soni 3 ga qoldiqsiz bo'linadi" ko'rinishida)
def bolinish_alomatlari(son):
    for n in range(2, 11):
        if not son % n:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")


bolinish_alomatlari(20)
