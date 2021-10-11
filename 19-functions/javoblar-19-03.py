"""
16/12/2020

Dasturlash asoslari

#19-dars: FUNCTIONS (FUNKSIYALAR)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
def juftmi(son):
    """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
    if son % 2:
        print(f"{son} toq son")
    else:
        print(f"{son} juft son")


juftmi(20)
juftmi(123)
