def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    """Avtomobil haqidagi ma'lumotlarni lug'at ko'rinishida qaytaruvchi funksiya"""
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rangi,
        "korobka": korobka,
        "yil": yili,
        "narh": narhi,
    }
    return avto


def avto_kirit():
    """Foydalanuvchiga avto_info funksiyasi yordamida bir nechta avtolar haqida ma'lumotlarni bitta ro'yxatga joylash imkonini beruvchi funksiya"""
    avtolar = []  # salondagi avtolar uchun bo'sh ro'yxat
    while True:
        print("\nQuyidagi ma'lumotlarni kiriting", end="")
        kompaniya = input("Ishlab chiqaruvchi: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobka: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narhi = input("Narhi: ")
        # Foydalanuvchi kiritdan ma'lumotlardan avto_info yordamida
        # lug'at shakllantirib, har bir lug'atni ro'yxatga qo'shamiz:
        avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
        # Yana avto qo'shish-qo'shmaslikni so'raymiz
        javob = input("Yana avto qo'shasizmi? (yes/no): ")
        if javob == "no":
            break
    return avtolar


def info_print(avto_info):
    """Avtomobillar haqida ma'lumotlar saqlangan lug'atni konsolga chiqaruvchi funksiya"""
    print(
        f"{avto_info['rang'].title()} {avto_info['kompaniya'].upper()} "
        f"{avto_info['model'].upper()}, {avto_info['korobka']} korobka, "
        f"{avto_info['yil']}-yil, {avto_info['narh']}$"
    )
