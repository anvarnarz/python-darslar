"""
21/01/2021

Dasturlash asoslari

#28-DARS. KLASSLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
class Talaba:
    """Talaba nomli klass yaratamiz"""
    def __init__(self,ism,familiya,tyil):
        """Talabaning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil
    
    def get_name(self):
        """Talabaning ismini qaytaradi"""
        return self.ism
    
    def get_lastname(self):
        """Talabaning familiyasini qaytaradi"""
        return self.familiya
    
    def get_fullname(self):
        """Talabaning ism-familiyasini qaytaradi"""
        return f"{self.ism} {self.familiya}"
    
    def get_age(self,yil):
        """Talabaning yoshini qaytaradi"""
        return yil-self.tyil
    
    def tanishtir(self):
        print(f"Ismim {self.ism} {self.familiya}. {self.tyil} yilda tu'gilganman")

talaba1 = Talaba("Alijon","Valiyev",2000)
print(talaba1.get_fullname())
print(talaba1.get_age(2021))








