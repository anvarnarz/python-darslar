"""
10/02/2021

Dasturlash asoslari

#33-DARS. FILES

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import pickle

with open('info','rb') as file:
    talaba1 = pickle.load(file)
    talaba2 = pickle.load(file)

print(talaba1)
print(talaba2)