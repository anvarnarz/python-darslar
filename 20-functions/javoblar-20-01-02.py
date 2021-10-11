"""
18/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def mijoz_info(ism, familiya, tyil, tjoy, email="", tel=None):
    """Mijoz haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    mijoz = {
        "ism": ism,
        "familiya": familiya,
        "tyil": tyil,
        "yoshi": 2020 - tyil,
        "tjoy": tjoy,
        "email": email,
        "telefon": tel,
    }
    return mijoz


print("Mijoz haqida ma'lumotlarni kiriting.")
mijozlar = []
while True:
    ism = input("Ismi: ")
    familiya = input("Familiyasi: ")
    tyil = int(input("Tug'ilgan yili: "))
    tjoy = input("Tug'ilgan joyi: ")
    email = input("Email: ")
    telefon = input("Telefon raqami: ")
    mijozlar.append(mijoz_info(ism, familiya, tyil, tjoy, email, telefon))
    javob = input("Davom etasizmi? (ha/yo'q)")
    if javob != "ha":
        break

print("Mijozlar:")
for mijoz in mijozlar:
    print(
        f"{mijoz['ism'].title()} {mijoz['familiya'].title()},"
        f"{mijoz['yoshi']} yoshda, telefoni: {mijoz['telefon']}"
    )
