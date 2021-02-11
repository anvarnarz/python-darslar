"""
10/02/2021

Dasturlash asoslari

#33-DARS. FILES

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
while True:
    book = input("Yaxshi koʻrgan kitobingizni kiriting (to'xtash uchun Enter bosing): ")
    if not book: break
    with open('amaliyot/books.txt','a') as file:
        file.write(book+'\n')