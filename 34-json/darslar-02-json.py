"""
14/02/2021

Dasturlash asoslari

#34-DARS. JSON

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

print(type(bemor))