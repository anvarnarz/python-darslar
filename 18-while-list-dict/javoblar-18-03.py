"""
13/12/2020

Dasturlash asoslari

#18-dars: WHILE VA RO'YXATLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
buyurtmalar = ["olma", "anjir", "uzum", "qovun"]
mahsulotlar = {"olma": 20000, "shaftoli": 25000, "tarvuz": 18000, "uzum": 22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar.keys():
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
