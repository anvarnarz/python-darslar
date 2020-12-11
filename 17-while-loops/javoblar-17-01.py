"""
10/12/2020

Dasturlash asoslari

#17-dars: WHILE

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

savol = "Sevgan kitobingizni kiriting"
savol += "(barcha kitoblarni kiritib bo'lgach 'exit' deb yozing): "

while True:
    kitob = input(savol)
    if kitob == 'exit':
        break
print('Rahmat!')       
