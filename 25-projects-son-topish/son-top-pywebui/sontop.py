import pywebio
from pywebio.input import input
from pywebio.output import put_text, put_buttons
import random
from time import sleep


def sontop(x=10):
    pywebio.output.clear(scope=- 1)
    tasodifiy_son = random.randint(1,x)
    while True:
        taxmin = int(input(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi?"))
        if taxmin<tasodifiy_son:
            put_text("Kattaroq son ayting!")
        elif taxmin>tasodifiy_son:
            put_text("Kichikroq son ayting!")
        else:
            put_text("Yutdingiz!")
            break

def sontop_pc(x=10):    
    global quyi, yuqori, taxmin
    quyi=1
    yuqori=x
    
    put_text(f"1 dan {x} gacha son o'ylang.\nSizga 3 soniya vaqt!")
    
    for i in [3,2,1,'Boshladik!']:
        put_text(str(i))
        sleep(1)        
    
    def guess():        
        pywebio.output.clear(scope=- 1)
        global taxmin       
        taxmin = random.randint(quyi,yuqori)
        put_text(f"Siz {taxmin} sonini o'yladingiz!")
        put_buttons(['Kattaroq','Togri','Kichikroq'], onclick=[katta,bingo,kichik])             
        pywebio.session.hold()
    
    def kichik():
        global yuqori
        yuqori = taxmin-1    
        guess()
    
    def katta():
        global quyi
        quyi = taxmin+1
        guess()
    
    def bingo(): 
        put_text("Men yutdim!")        
    
    guess()      

