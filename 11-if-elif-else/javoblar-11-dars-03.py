"""
25/11/2020

Dasturlash asoslari

#11-dars: if-elif-else

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

x = float(input("Birinchi sonni kiriting: "))
y = float(input("Ikkinchi sonni kiriting: "))
if x == y:
    print(f"{x}={y}")
elif x < y:
    print(f"{x}<{y}")
else:
    print(f"{x}>{y}")
