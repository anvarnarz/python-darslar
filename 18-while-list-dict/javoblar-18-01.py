"""
13/12/2020

Dasturlash asoslari

#18-dars: WHILE VA RO'YXATLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
savat = []
while True:
    mahsulot = input("Savatga mahsulot qo'shing:")
    savat.append(mahsulot)
    javob = input("Yana mahsulot qo'shasizmi?(ha/yo'q)")
    if javob != "ha":
        break
print("Dastur tugadi!")
