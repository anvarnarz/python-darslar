"""
11/03/2021

Dasturlash asoslari

#39-DARS. PYTHON TASHQI KUTUBXONASI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# pip install googletrans==3.1.0a0
from googletrans import Translator
tarjimon = Translator()

msg = "Tarjima uchun so'z kiriting (chiqib ketish uchun \"q\" deb yozing): "
while True:
    text = input(msg)
    if text == "q":
        break
    else:
        tarjima = tarjimon.translate(text, src='uz', dest='en')
        print(tarjima.text)    