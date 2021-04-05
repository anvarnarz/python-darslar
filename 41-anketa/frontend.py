from pywebio.input import input, input_group

def getInfo():
    info = input_group("Fuqaro haqida ma'lumot",[
      input('Ism', name='ism'),
      input('Familiya', name='familiya',),
      input('Otasining ismi', name='otasi',),
      input("Tug'ilgan yil", name='tyil',),
      input("Tug'ilgan kun", name='tkun',),
      input("Tug'ilgan oy", name='toy',),
      input('Telefon raqami', name='telefon',),
      input('Pasport seriyasi', name='seriya',),
      input('Pasport raqami', name='pass_raqam',),
      input('Passport berilgan sana', name='pass_sana',)
    ])
    return info
