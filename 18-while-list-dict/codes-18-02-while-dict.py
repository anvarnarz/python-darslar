"""
13/12/2020

Dasturlash asoslari

#18-dars: WHILE VA RO'YXATLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
print("Do'stlaringiz yoshini saqlaymiz.")
dostlar = {}
ishora = True
while ishora:
    ism = input("Do'stingiz ismini kiriting: ")
    yosh = input(f"{ism.title()}ning yoshini kiriting: ")
    dostlar[ism] = int(yosh)

    javob = input("Yana ma'lumot qo'shasizmi? (ha/yo'q)")
    if javob == "yo'q":
        ishora = False

for ism, yosh in dostlar.items():
    print(f"{ism.title()} {yosh} yoshda")
