import json
personaje = {
    "nombre": "Goku",
    "nivel": 99,
    "transformaciones": ["Sayan", "God", "Blue"],
    "activo": True
}
    
class personaje_de_anime:
    def __init__(self,nombre,nivel,transfomaciones,activo):
        self.nombre = nombre 
        self.nivel =nivel 
        self.transformacion = transfomaciones
        self.activo = activo
        
    def guardar_datos(self):
        info = {
            "nombre": self.nombre,
            "nivel": self.nivel,
            "transformaciones" : self.transformacion,
            "activo": self.activo
            
        }
        with open("datos.json","w") as archivo:
            json.dump(info,archivo,indent=4)
        print("archivo guardado")
        
    def iniciar(self):
        while True:
            print("opciones:")
            print("1-cambiar nombre:")
            print("2-cambiar nivel")
            print("3-cambiar transformaciones")
            print("4-cambiar estado")
            print("5-salir")
            accion = input("que eliges: ").lower().strip()
            if accion == "5":
                print("ok")
                break
            elif accion == "1":
                nuevo_nombre = input("que nobre vas a usar: ")
                self.nombre = nuevo_nombre 
                self.guardar_datos()
            
            elif accion == "2":
                while True:
                    try:
                        nuevo_nivel = int(input("Cual es el nuevo nivel "))
                        if nuevo_nivel <= 0:
                            continue
                        break
                    except ValueError:
                        print("solo numeros")
                self.nivel = nuevo_nivel
                self.guardar_datos
            elif accion == "3":
                agregar = input("que transformacion vas a agragar: ")
                self.transformacion.append(agregar)
                self.guardar_datos()
            elif accion == "4":
                print("1-vivo")
                print("2-muerto")
                estado = input("en que estado esta: ")
                if estado == "1":
                    self.activo = True
                    self.guardar_datos()
                    
                elif estado == "2":
                    self.activo = False
                    self.guardar_datos()
                    
                else:
                    print("no existe esta alternativa")
                    
            else:
                print("vuelva a intetar")


goku = personaje_de_anime("Goku", 99, ["Sayan", "God", "Blue"], True)
goku.guardar_datos()
goku.iniciar()
