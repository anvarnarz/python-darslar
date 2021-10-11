"""
29/03/2021

Dasturlash asoslari

15-DARS: To'plamlar

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
# To'plamga element qo'shish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.add("banan")
print(mevalar)
mevalar.update(["anor", "qovun"])
print(mevalar)

# Element o'chirish
mevalar = {"anjir", "olma", "uzum", "banan", "anor"}
mevalar.discard("anjir")
print(mevalar)
mevalar.remove("banan")
print(mevalar)

sonlar = {1, 2, 3, 4, 5, 6}
sonlar.discard(7)
print(sonlar)
sonlar.remove(7)
print(sonlar)

sonlar = {1, 2, 3, 4, 5, 6}
son = sonlar.pop()
print(son)
print(sonlar)
