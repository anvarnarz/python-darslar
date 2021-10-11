"""
8/11/2020

Dasturlash asoslari

#05-dars: STRING (MATN)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

kocha = "Bog'bon"
mahalla = "Sog'bon"
tuman = "Bodomzor"
viloyat = "Samarqand"

# Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
# Diqqat uzun kodlarni \ belgisi yordamida keyingi qatorga
# ko'chirish mumkin
print(
    kocha
    + " ko'chasi, "
    + mahalla
    + " mahallasi, "
    + tuman
    + " tumani, "
    + viloyat
    + " viloyati"
)

# Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
print("Iltimos, quyidagi ma'lumotlarni kiriting:")
kocha = input("Ko'changiz: ")
mahalla = input("Mahallangiz: ")
tuman = input("Tumaningiz: ")
viloyat = input("Viloyatingiz: ")
print(
    kocha
    + " ko'chasi, "
    + mahalla
    + " mahallasi, "
    + tuman
    + " tumani, "
    + viloyat
    + " viloyati"
)

# Yuqoridagi matnni konsolga chiqarishda har bir verguldan keyin yangi qatorga yozing
print(
    kocha
    + " ko'chasi,\n"
    + mahalla
    + " mahallasi,\n"
    + tuman
    + " tumani,\n"
    + viloyat
    + " viloyati"
)

# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)

# manzil ga biz yuqorida o'rgangan metodlarni qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())
