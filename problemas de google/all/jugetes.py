
class jugetes:
    def __init__(self,nombre,marca):
        self.nombre = nombre
        self.marca = marca
        
j1 = jugetes("Bloques", "LEGO")
j2 = jugetes("Carrito", "LEGO")
j3 = jugetes("Muñeca", "Barbie")

almacen_correcto = [[j1, j2], [j1, j1]]
almacen_incorrecto = [[j1, j3], [j2, j1]]

def verifica(lista):
    verificado = all(i.marca == "LEGO" for jugetes in lista for i in jugetes)
    print(verificado)
    
verifica(almacen_incorrecto)
