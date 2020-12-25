"""
24/12/2020

Dasturlash asoslari

#23-dars: MODULLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

import avto_info_lib as avtoil

avtolar = avtoil.avto_kirit()

for avto in avtolar:
    avtoil.info_print(avto)