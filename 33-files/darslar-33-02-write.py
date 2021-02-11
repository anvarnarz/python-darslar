"""
10/02/2021

Dasturlash asoslari

#33-DARS. FILES

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
   
faylnomi = 'new_file.txt'
ism = 'Olimjon Hasanov'
tyil = 2004
with open(faylnomi,'w') as fayl:
    fayl.write(ism+'\n')
    fayl.write(str(tyil)+'\n')
    
with open(faylnomi,'a') as fayl:
    fayl.write('Alijon Valiyev\n')
    fayl.write('2000')