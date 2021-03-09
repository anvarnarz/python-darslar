"""
09/03/2021

Dasturlash asoslari

#38-DARS. PYTHON KUTUBXONASI

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
from pprint import pprint
import json

filename = 'bemor.json'
with open(filename) as f:
    bemor = json.load(f)

# pprint(bemor)
pprint(bemor)

import requests
r = requests.get('https://api.github.com')

pprint(r.json())