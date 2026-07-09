import json

from her import pedir_info_entero,pedir_info_flotante,modificar_almacen,crear_contraseña
from tienda_de_gatos import producto
import datetime
class historial:
    def __init__(self,producto,cantidad):
        self.nombre = producto
        self.cantidad = cantidad
        self.fecha = datetime.now()

class usuario:
    def __init__(self,nombre):
        self.nombre = nombre
        self.historial = []
        
    def historial_de_compra(self,producto,cantidad):
        cosas = historial(producto,cantidad)
        self.historial.append({"producto":cosas.nombre,"cantidad": cosas.cantidad,"fecha":cosas.fecha.strftime("%d/%m/%Y %H:%M:%S")})
        
    def comprar(self,dueño,tienda):
        modificar_almacen(tienda,"cliente",dueño)
        
        
    
            

class dueño:
    def __init__ (self,nombre,contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        self.ganancia = 0
        
    def ganar_mone(self,producto,cantidad):
        costo = producto.precio * cantidad
        self.ganancia += costo
    def registro_del_dueño(self):
        info = {
            "nombre":self.nombre,
            "contraseña": self.contraseña,
            "ganancia": self.ganancia
            }
        with open ("usuario.json","w") as archivo:
            json.dump(info,archivo,indent= 4)       

    
        
    