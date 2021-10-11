"""
01/01/2021

Dasturlash asoslari

#24-dars: FUNKSIYALAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import random as r

sonlar = r.sample(range(100), 10)  # 0-99 oralig'ida 10 ta tasodifiy sonlar
# print(sonlar)
def juftmi(x):
    """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
    return x % 2 == 0


# juft_sonlar = list(filter(juftmi,sonlar))
# print(juft_sonlar)

juft_sonlar = list(filter(lambda x: x % 2 == 0, sonlar))
# print(juft_sonlar)

mevalar = ["olma", "anor", "anjir", "shaftoli", "o'rik", "tarvuz", "qovun", "banan"]
harf = "o"
mevalar_b = list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar_b)

mevalar2 = list(filter(lambda meva: len(meva) <= 5, mevalar))
print(mevalar2)

list(filter(lambda meva: (meva.startswith("a") and meva.endswith("r")), mevalar))

# # sonlar = r.sample(range(100),10)
# # juft = [son for son in sonlar if son%2==0]
