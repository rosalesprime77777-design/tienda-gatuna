import json


class producto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre 
        self.cantidad = cantidad
        self.precio = precio

class tienda:
    def __init__(self):
        self.almacen = []
        
        
    def crear_usuario(self):
        nombre = input("cual es tu nombre: ")
        contraseña = input("cual sera tu contraseña; ")
        info = {
            "nombre":nombre,
            "contraseña": contraseña,
            "ganancia": 0
        }
        with open ("usuario.json","w") as archivo:
            json.dump(info,archivo,indent= 4)
            
    def iniciar(self)