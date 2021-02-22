"""
22/02/2021

Dasturlash asoslari

#36-DARS. FUNKSIYALARNI TEKSHIRISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

def get_full_name(ism, familiya, otasi=""):
    if otasi:
        return f"{ism} {otasi} {familiya}".title()   
    else:
        return f"{ism} {familiya}".title()

# print(get_full_name('alijon','valiyev'))
# print(get_full_name('hasan','husanov','olimovich'))