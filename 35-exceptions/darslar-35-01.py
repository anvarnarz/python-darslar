"""
18/02/2021

Dasturlash asoslari

#35-DARS. XATOLAR BILAN ISHLASH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


## Xatolar
# yosh = input("Yoshingizni kiriting: ")
# yosh = int(yosh)
# print(f"Siz {2021-yosh} yilda tug'ilgansiz")

## try-except
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)  
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")  
# except ValueError:
#     print("Butun son kiritmadingiz")

## try-except-else
# print("Dastur Tugadi!")
# yosh = input("Yoshingizni kiriting: ")
# try:
#     yosh = int(yosh)    
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2021-yosh} yilda tug'ilgansiz")

# x,y=5,10
# try:
#    y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
       
# mevalar = ['olma','anor','anjir','uzum']
# try:
#     print(mevalar[7])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")

# user = {"username":"sariqdev",
#         "status":"admin",
#         "email":"admin@sariq.dev",
#         "phone":"99897123456"}

# key="tel"
# try:
#     print(f'Foydalanuvchi: {user[key]}')
# except KeyError:
#     print("Bunday kalit mavjud emas")

# filename = "data.txt" # bunday fayl mavjud emas
# with open(filename) as f:
#     text = f.read()

# filename = "data.txt" # bunday fayl mavjud emas
# try:
#     with open(filename) as f:
#         text = f.read()
# except FileNotFoundError:
#     print(f"Kechirasiz, {filename} fayli mavjud emas. Bosh fayl tanlang.")
        
# n = input("Butun son kiriting: ")
# try:
#     n = int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz")
# except ZeroDivisionError:
#     print("0 ga bo'lib bo'lmaydi")
# else:
#     pass

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         print(f"{filename} mavjud emas")
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar 

# import json
# files = ['talaba1.json','talaba2.json','talaba3.json','talaba4.json']
# for filename in files:
#     try:
#         with open(filename) as f:
#             talaba = json.load(f)        
#     except FileNotFoundError:
#         pass
#     else:
#         print(talaba['ism'])
#         # fayl ustida turli amallar 