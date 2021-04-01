"""
18/02/2021

Dasturlash asoslari

#35-DARS. XATOLAR BILAN ISHLASH

Muallif: Anvar Narzullaev

Web sahifa: https://python.sariq.dev
"""
try:
     x = int( input( "son kiriting: " ) )
     y = int( input( "yana son kiriting: " ) )
     print( x, '/', y, '=', x/y )     
except ZeroDivisionError:
     print( "0 ga bo'lib bo'lmaydi" )
except ValueError:
     print( "Bu son emas" )
except:
     print( "Xato yuz berdi!" )
