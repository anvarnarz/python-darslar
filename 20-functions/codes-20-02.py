"""
17/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def toliq_ism_yasa(ism, familiya, otasining_ismi=""):
    """Toliq isma qaytaruvchi funksiya"""
    if otasining_ismi:
        toliq_ism = f"{ism} {otasining_ismi} {familiya}"
    else:
        toliq_ism = f"{ism} {familiya}"
    return toliq_ism.title()


talaba1 = toliq_ism_yasa("olim", "hakimov")
talaba2 = toliq_ism_yasa("hakim", "olimov", "abrorovich")
print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")
