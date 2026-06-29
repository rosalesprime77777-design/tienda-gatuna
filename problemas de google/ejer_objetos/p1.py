import json

class Auto:
    def __init__(self, modelo, velocidad_max):
        self.modelo = modelo
        self.velocidad_max = velocidad_max
        
garaje_ram = {
    "auto_1": Auto("Ferrari", 340),
    "auto_2": Auto("Lamborghini", 350)
}

def guardar_datos(almacen):
    son_goku = {}
    for clave,objeto in almacen.items():
        son_goku[clave] = {
            "velocida": objeto.velocidad_max,
            "modelo": objeto.modelo
        }
        
    with open("cochera.json","w") as f:
        json.dump(son_goku,f,indent= 4)
        
        
guardar_datos(garaje_ram)