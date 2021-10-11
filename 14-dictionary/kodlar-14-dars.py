"""
03/12/2020

Dasturlash asoslari

#14-dars: Dictionary (Lug'at)

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
car_0 = {"model": "ferrari", "rang": "qizil"}
print(car_0["model"])
print(car_0["rang"])

# # Lug'atda istalgan ma'lumot turlarini saqlash mumkin
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")

# # Yangi kalit so'z va qiymat qo'shish
# talaba_0['kurs'] = 4
# talaba_0['fakultet'] = 'informatika'
# talaba_0['ism'] = 'abdulloh'

# # Bo'sh lug'at
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # Qiymatni yangilash
# talaba_1['kurs'] = 4
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

# # Kalit so'z-qiymat ni o'chirib tashlashj
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(talaba_0)
# del talaba_0['yosh']
# print(talaba_0)

# # Lu'gatlarni bir nechta qatorda yozish
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# # get() metodi
# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")

# # phone = telefonlar['hasan']
# # print(f"Hasanning telefoni {phone}")

# phone = telefonlar.get('hasan','Bunday ism mavjud emas')
# print(phone)

# phone = telefonlar.get('hasan')
# print(phone)
