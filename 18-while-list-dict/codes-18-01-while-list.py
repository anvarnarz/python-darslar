"""
13/12/2020

Dasturlash asoslari

#18-dars: WHILE VA RO'YXATLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
ismlar = []
n = 1  # ismlarni sanash uchun o'zgaruvchi
while True:
    savol = f"{n}-do'stingiz ismini kiriting:"
    ism = input(savol)
    ismlar.append(ism)
    takrorlash = input("Yana ism qo'shasizmi? (ha/yo'q)")
    n += 1
    if takrorlash != "ha":
        break


print("Do'stlaringiz ro'yxati:")
for ism in ismlar:
    print(ism.title())
