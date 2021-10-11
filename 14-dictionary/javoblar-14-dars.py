"""
03/12/2020

Dasturlash asoslari

#14-dars: DICTIONARY

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

otam = {"ismi": "mavlutdin", "tyil": 1954, "viloyat": "samarqand"}
tyil = otam["tyil"]
vil = otam["viloyat"]
print(
    f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan"
)

taomlar = {
    "ali": "osh",
    "vali": "shashlik",
    "hasan": "lag'mon",
    "husan": "mastava",
    "olim": "somsa",
}

taom = taomlar["ali"]
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "string": "Matn",
    "list": "Ro'yxat",
    "tuple": "O'zgarmas ro'yxat",
}
# print(python_izohli_lugati['tuple'])

kalit = input("Kalit so'z kiriting:").lower()
print(python_izohli_lugati.get(kalit, "Bunday so'z mavjud emas"))

kalit = input("Kalit so'z kiriting:").lower()
tarjima = python_izohli_lugati.get(kalit)
if tarjima == None:
    print("Bunday so'z mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
