"""
06/12/2020

Dasturlash asoslari

#16-dars: NESTING

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

# LUG'AT ICHIDA RO'YXAT
dasturchilar = {
    "ali": ["python", "c++"],
    "vali": ["html", "css", "js"],
    "hasan": ["php", "sql"],
    "husan": ["python", "php"],
    "maryam": ["c++", "c#"],
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end="")
    for til in tillar:
        print(f"{til.upper()} ", end="")
