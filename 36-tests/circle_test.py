"""
22/02/2021

Dasturlash asoslari

#36-DARS. FUNKSIYALARNI TEKSHIRISH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
import unittest
from circle import getArea, getPerimeter

class CircleTest(unittest.TestCase):
    def test_area(self):
        self.assertAlmostEqual(getArea(10), 314.159)
        self.assertAlmostEqual(getArea(3),28.27431)
    def test_perimeter(self):
        self.assertAlmostEqual(getPerimeter(10), 62.8318)
        self.assertAlmostEqual(getPerimeter(4), 25.13272)
        
# if __name__ == '__main__':
    # unittest.main()
unittest.main()