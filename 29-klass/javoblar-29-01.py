"""
22/01/2021

Dasturlash asoslari

#29-DARS. OBYEKTLAR BILAN ISHLASH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

class Car:
    def __init___(self,make,model,rang,korobka,narh):
        self.make = make
        self.model = model
        self.rang = rang
        self.korobka = korobka
        self.narh = narh
        self.km = 0
    
    def get_make(self):
        return self.make
    
    def get_model(self):
        return self.model
    
    def get_rang(self):
        return self.rang
    
    def get_gear(self):
        return 
