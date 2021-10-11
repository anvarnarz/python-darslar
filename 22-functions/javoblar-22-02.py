"""
24/12/2020

Dasturlash asoslari

#22-dars: *args va **kwargs

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""


def talaba_info(ism, familiya, **kwargs):
    kwargs["ism"] = ism
    kwargs["familiya"] = familiya
    return kwargs


talaba = talaba_info("olim", "olimov", tyil=1995, fakultet="IT", yonalish="AT")
