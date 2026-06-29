class jugetes:
    def __init__(self, nombre, marca):
        self.nombre = nombre
        self.marca = marca


j1 = jugetes("Bloques", "LEGO")
j2 = jugetes("Barco", "LEGO")
j3 = jugetes("Muñeca", "Barbie")  
j4 = jugetes("Carrito", "LEGO")
almacen_perfecto = [[j1, j2], [j3, j1]]  # j3 se ignora. j1 y j2 empiezan con 'B'.
almacen_con_error = [[j1, j4], [j3, j2]]

def palabra(palabra,letra):
    for i in palabra:
        if palabra[0] == letra:
            return True
    return False

def validar(listas):
    lista_limpia = []
    for i in listas:
        for marca in i:
            if marca.marca == "LEGO":
                lista_limpia.append(marca)
                
    validar = all(palabra(i,"B") for a in lista_limpia)
    print(validar)
    
validar(almacen_con_error)
