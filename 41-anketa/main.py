from pywebio.output import put_html, put_file
from pywebio.session import hold
from frontend import getInfo
from backend import fillDoc

title = "<h1 style=\"text-align:center\">Ўзбекистон Республикаси фуқаросининг\
  хорижга чиқиш биометрик паспортини расмийлаштириш учун АНКЕТА</h1>"
put_html(title)

userInfo = getInfo()
filename = fillDoc(userInfo)

text = "<h3>Анкета тайёр. Юклаб олиш учун қуйидаги боғламани босинг.</h3>"
put_html(text)

with open(filename,'rb') as fayl:
    anketa = fayl.read()        
    put_file(filename,content=anketa)
    hold()