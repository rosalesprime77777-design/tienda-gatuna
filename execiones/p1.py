def descuento(precio,descuento):
    if precio <= 0:
        raise ValueError("no puede ser numeros negatigos o nulos")
    res = (precio * descuento)/100
    print(res)
    
descuento(-100,10)