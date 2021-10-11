"""
17/12/2020

Dasturlash asoslari

#20-dars: FUNKSIYADAN QIYMAT QAYTARISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
    avto = {
        "kompaniya": kompaniya,
        "model": model,
        "rang": rangi,
        "korobka": korobka,
        "yil": yili,
        "narh": narhi,
    }
    return avto


avto1 = avto_info("GM", "Malibu", "Qora", "Avtomat", 2018)
avto2 = avto_info("GM", "Gentra", "Oq", "Mexanika", 2016, 15000)
avtolar = [avto1, avto2]
print("Onlayn bozordagi mavjud avtomashinalar:")
for avto in avtolar:
    if avto["narh"]:
        narh = avto["narh"]
    else:
        narh = "Noma'lum"
    print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")
