import json
from her import crear_contraseña
class producto:
    def __init__(self,nombre,cantidad,precio):
        self.nombre = nombre 
        self.cantidad = cantidad
        self.precio = precio
        
    def retirar(self,cantidad):
        self.cantidad -= cantidad
        
    def aumentar(self,cantidad):
        self.cantidad += cantidad
        
        


class tienda_gatuna:
    def __init__(self):
        self.almacen = {}
    def guardar_registro(self):
        texto_limpio = {}
        for nombre , objeto in self.almacen.items():
            texto_limpio[nombre]= {
                "nombre" : objeto.nombre,
                "precio": objeto.precio,
                "cantidad" : objeto.cantidad
            }
        with open("almacen.json","w") as f: 
            json.dump(texto_limpio,f,indent=4)
            
    def registro_almacen(self):
        with open ("registro.json","w") as f : 
            json.dump(self.almacen,f,indent= 4)
            
    def iniciar(self):