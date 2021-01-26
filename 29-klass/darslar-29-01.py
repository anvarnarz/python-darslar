"""
22/01/2021

Dasturlash asoslari

#29-DARS. OBYEKTLAR BILAN ISHLASH

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
        self.bosqich = 1
    
    def get_name(self):
        return self.ism    
    
    def get_info(self):
        """Talaba haqida ma'lumot"""
        return f"{self.ism} {self.familiya}. {self.bosqich}-bosqich talabasi "
    
    def set_bosqich(self,bosqich):
        """Talabaning kursini yangilovchi metod"""
        self.bosqich = bosqich
        
    def update_bosqich(self):
        """Talabanining bosqichini 1taga ko'paytirish"""
        self.bosqich += 1        
    
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

# talaba1 = Talaba("Alijon","Valiyev",2000)
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())
# talaba1.update_bosqich() # 1 bosqichga oshiramiz
# print(talaba1.get_info())

# # talaba1.set_bosqich(3)
# # print(talaba1.bosqich)