"""
04/12/2020

Dasturlash asoslari

#15-dars: LUG'AT BILAN ISHLASH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
python_words = {
    "integer": "Butun son",
    "float": "O'nlik son",
    "boolean": "Mantiqiy qiymat",
    "for": "Biror amalni qayta-qayta bajarish tsikli",
    "if": "Shartlarni tekshirish operatori",
}

for key, value in sorted(python_words.items()):
    print(f"{key.title()} - {value}")
