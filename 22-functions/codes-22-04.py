"""
24/12/2020

Dasturlash asoslari

#22-dars: *args va **kwargs keywords

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def avto_info(kompaniya, model, **malumotlar):
    """Avto haqidagi ma'lumotlarni lug'at ko'rinishdia qaytaruvchi funksiya"""
    malumotlar["kompaniya"] = kompaniya
    malumotlar["model"] = model
    return malumotlar


avto1 = avto_info("GM", "malibu", rang="qora", yil=2018)
avto2 = avto_info("Kia", "K5", rang="qizil", narh=35000, yil=2020, korobka="avtomat")
