from sontop import SonTop, SonTopPC
from pywebio.output import popup

game1 = SonTop()
game1.play()
taxminUser = game1.getResult()

game2 = SonTopPC()
game2.play()
if game2.gameOver:
    taxminPC = game2.getResult()


if taxminUser<taxminPC:
    popup("Tabriklayman!",f"Siz {taxminUser} ta taxmin bilan yutdingiz!")
elif taxminUser>taxminPC:
    popup("G'alaba!",f"Men {taxminPC} ta taxmin bilan yutdim!")
else:
    popup("Durran", f"Ikkalamizda ham {taxminPC} ta taxmin.")
