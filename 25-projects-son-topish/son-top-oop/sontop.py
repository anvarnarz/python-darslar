import pywebio
from pywebio.input import input
from pywebio.output import put_text, put_buttons
import random
from time import sleep

class SonTop:
    def __init__(self,x=10):
        self.x = x
        self.__taxminlar = 0
    def play(self):
        pywebio.output.clear(scope=- 1)
        tasodifiy_son = random.randint(1,self.x)
        while True:
            self.__taxminlar += 1
            taxmin = int(input(f"Men 1 dan {self.x} gacha son o'yladim. Topa olasizmi?"))
            if taxmin<tasodifiy_son:
                put_text("Kattaroq son ayting!")
            elif taxmin>tasodifiy_son:
                put_text("Kichikroq son ayting!")
            else:
                put_text("Yutdingiz!")
                break
    def getResult(self):
        return self.__taxminlar
  
class SonTopPC:
    def __init__(self,x=10):
        self.x = x
        self.__quyi = 1
        self.__yuqori = x
        self.__taxmin = None
        self.__taxminlar = 0
        self.gameOver = False
        
    def guess(self):
        self.__taxminlar += 1
        yuqori = self.__yuqori
        quyi = self.__quyi
        pywebio.output.clear(scope=- 1)    
        self.__taxmin = random.randint(quyi, yuqori)
        put_text(f"Siz {self.__taxmin} sonini o'yladingiz!")
        put_buttons(['Kattaroq','Togri','Kichikroq'], onclick=[self.katta, self.bingo,self.kichik])
        pywebio.session.hold()
    
    def kichik(self):
        self.__yuqori = self.__taxmin-1    
        self.guess()
    
    def katta(self):        
        self.__quyi = self.__taxmin+1
        self.guess()
    
    def bingo(self): 
        put_text("Men yutdim!")
        self.gameOver = True        
    
    def play(self):
        put_text(f"1 dan {self.x} gacha son o'ylang.\nSizga 3 soniya vaqt!")    
        for i in [3,2,1,'Boshladik!']:
            put_text(str(i))
            sleep(1)
        self.guess()
    
    def getResult(self):
        return self.__taxminlar 

