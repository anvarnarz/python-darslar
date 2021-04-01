print("x/y hisoblovchi dastur")
while True:
    x = input( "x ni kiriting: " )
    if x.isdigit():
        x=int(x) 
    else:
        print("Bu son emas!")
        continue
    
    y = input( "y ni kiriting: " )
    if y.isdigit():
        y=int(y) 
    else:
        print("Bu son emas!")
        continue
    
    if y==0:
        print("y 0 bo'lishi mumkin emas!")
        continue
    else:  
        print( x, '/', y, '=', x/y )
        break