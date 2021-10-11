"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

kinolar = {
    "ali": ["Terminator", "Rambo", "Titanic"],
    "vali": ["Tenet", "Inception", "Interstellar"],
    "hasan": ["Abdullajon", "Bomba", "Shaytanat"],
    "husan": ["Mahallada duv-duv gap", "John Wick"],
}

for ism, kinolar in kinolar.items():
    print(f"\n{ism.title()}ning sevimli kinolari:")
    for kino in kinolar:
        print(kino)
