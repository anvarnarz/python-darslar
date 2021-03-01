"""
27/02/2021

Dasturlash asoslari

#37-DARS. KLASSNI TEKSHIRISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import unittest
from cars import Car
make = "GM"
model = "Malibu"
year = 2020
km = 10
price = 40000
avto = Car(make,model,year,km,price)

class CarTest(unittest.TestCase):
    """Car klassini tekshirish uchun test"""
    
    def test_create(self):        
        # avto1 obyektini km va narhini bermasdan yaratamiz
        avto1 = Car("toyota","camry",2020)
        # Qiymatlar mavjudligini assertIsNotNone metodi bilan tekshiramiz
        self.assertIsNotNone(avto1.make)
        self.assertIsNotNone(avto1.model)
        self.assertIsNotNone(avto1.year)
        # Qiymat mavjud emasligini assertIsNone metodi bilan tekshiramiz
        self.assertIsNone(avto1.price)
        # Qiymat tengligini assertEquals metodi bilan tekshiramiz
        self.assertEquals(0,avto1.get_km())
        # Avtomobil narhini ham ko'rsatamiz
        avto2 = Car("toyota","camry",2020,price=75000)
        self.assertEquals(75000,avto2.price)
        
unittest.main()      