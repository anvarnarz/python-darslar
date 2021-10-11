"""
25/11/2020

Dasturlash asoslari

#11-dars: if-elif-else

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

son = int(input("Istalgan butun son kiriting: "))

for n in range(2, 11):
    if not (son % n):
        print(f"{son} soni {n} ga qoldiqsiz bo'linadi")
