"""
10/12/2020

Dasturlash asoslari

#17-dars: INPUT() VA WHILE

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

input()
ism = input("Ismingiz nima? ")
savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
yosh = input(savol)
yosh = int(yosh)
height = input("Bo'yingiz necha metr? ")
height = float(height)

# while()
son = 1 # son ga 1 qiymatini beramiz
while son<=5: # toki son 5 dan kichik yoki teng ekan...
    print(son, end=' ') # son ni konsolga chiqaramiz
    son = son + 1
    #son += 1 # songa 1 qo'shamiz


# # while and input
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print('Dastur tugadi')


# # ishora
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)    
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)
# print('Dastur to\'xtadi!')

# break while
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True: # abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break # tsiklni to'xtatish
#     else:
#         print(float(qiymat)**2)
# print('Dastur tugadi!')
# # break for

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")

# CONTINUE
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# # # Continue while
# son = 0
# while son<10:
#     son += 1
#     if son%2==0:
#         continue
#     else:
#         print(son)

# infinite loop
# son = 0
# while son<10:
#     if son%2!=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:    
#     if son%2!=0:
#         continue
#     else:
#         print(son)
#     son += 1

# son = 1
# while son>0: 
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)
    
        