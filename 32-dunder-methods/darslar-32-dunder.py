"""
03/02/2021

Dasturlash asoslari

#32-DARS. DUNDER METODLAR

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""

class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    def __str__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$"
    
    def __repr__(self):
        """Obyekt haqida ma'lumot"""
        return f"Avto: {self.make} {self.model}. {self.narh}$" 
    
    def __eq__(self,boshqa_avto):
        return self.narh == boshqa_avto.narh
    
    def __lt__(self,boshqa_avto):
        return self.narh<boshqa_avto.narh
    
    def __le__(self,boshqa_avto):
        return self.narh<=boshqa_avto.narh
    
    def get_info(self):
        return f"{self.rang} {self.make} {self.model}.{self.yil}-yil. Narhi:{self.narh}$"

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self,name):
        self.name = name
        self.avtolar = []

    def __repr__(self):
        return f"{self.name} avtosaloni"
    
    def __len__(self):
        return len(self.avtolar)
    
    def __getitem__(self,index):
        return self.avtolar[index]
    
    def __setitem__(self,index,value):
        if isinstance(value,Avto):
            self.avtolar[index]=value
    
    def __add__(self,qiymat):
        if isinstance(qiymat,AvtoSalon):
            yangi_salon =  AvtoSalon(f"{self.name} {qiymat.name}")
            yangi_salon.avtolar = self.avtolar + qiymat.avtolar
            return yangi_salon
        elif isinstance(qiymat,Avto):
            self.add_avto(qiymat)
        else:
            print(f"AvtoSalon ga {type(qiymat)} qo`shib bo`lmaydi")
    
    def __call__(self,*param):
        if param:
            for avto in param:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]
    
    def add_avto(self,*qiymat):
        for avto in qiymat: 
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto obyketini kiriting")

    def get_list(self):
        return [avto for avto in self.avtolar]

    