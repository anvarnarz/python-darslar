from pywebio.input import input, FLOAT
from pywebio.output import put_text
from math import pi

def doira():
    r = input("Doira radiusini kiriting：", type=FLOAT)    
    yuza = pi*(r**2)
    per = 2*pi*r    
    put_text(f"Doira yuzi {yuza}ga,\nperimetri {per}ga teng")  

doira()