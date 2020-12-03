"""
03/12/2020

Dasturlash asoslari

#14-dars: DICTIONARY

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

otam = {'ismi':'mavlutdin', 'tyil':1954,'viloyat':'samarqand'}
tyil = otam['tyil']
vil = otam['viloyat']
print(f"Otamning ismi {otam['ismi'].title()}, {tyil}-yilda, {vil.title()} viloyatida tug'ilgan")

taomlar = {
    'ali':'osh',
    'vali':'shashlik',
    'hasan':"lag'mon",
    'husan':"mastava",
    'olim':"somsa"
    }

taom = taomlar['ali']
print(f"Alining sevimli taomi {taom}")

python_izohli_lugati = {
    'integer':"Butun son. Butun sonlarni ham o'zgaruvchida saqlash,\n ularning ustida qo'shish (+), ayirish (-),\n ko'paytirish(*), bo'lish (/) \n kabi arifmetik amalarni bajarish mumkin",
    'float':"Pythonda o'nlik sonlar floating point numbers yoki qisqa qilib floats deyiladi.",
    'string':"Matn, Pythondagi eng mashxur ma'lumot turlaridan biri."}
print(python_izohli_lugati['integer'])