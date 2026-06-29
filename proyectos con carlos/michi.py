class michi():
    def __init__(self):
        self.bloques = [1,2,3,4,5,6,7,8,9]
        self.claves = {
            "res1" : [1,2,3],
            "res2" : [4,5,6],
            "res3" : [7,8,9],
            "res4" : [1,4,7],
            "res5" : [2,5,8],
            "res6" : [3,6,9],
            "res7" : [1,5,9],
            "res8" : [3,5,7],
                       }
        
    def tablero(self):
        print(f"{self.bloques[0]}_|_{self.bloques[1]}_|_{self.bloques[2]}")
        print(f"{self.bloques[3]}_|_{self.bloques[4]}_|_{self.bloques[5]}")
        print(f"{self.bloques[6]}_|_{self.bloques[7]}_|_{self.bloques[8]}") 
        
    def modificar(self,num,signo):
        i = num - 1
        self.bloques[i] = signo
        
        
class jugador:
    def __init__(self,nombre):
        self.nombre = nombre
        self.elejidos = []
        self.claves = {
            "res1" : [1,2,3],
            "res2" : [4,5,6],
            "res3" : [7,8,9],
            "res4" : [1,4,7],
            "res5" : [2,5,8],
            "res6" : [3,6,9],
            "res7" : [1,5,9],
            "res8" : [3,5,7],
                       }
        
    def agregar(self,num):
        self.elejidos.append(num)
        
    def validar(self):
        for i in self.claves:
            v = self.claves[i]
            if all(num in self.elejidos for num in v):
                return True
        return False
    
    def turno(self,juego):
        while True:
            try:
                per = int(input(f"que bloque elijes {self.nombre} (para terminar escrive 2012): "))
                if per == 2012:
                    return 2012
                elif per > 9 or per <= 0:              
                    continue
                elif juego.bloques[per-1] == "x" or juego.bloques[per-1] == "O":
                    print("no intente hacer trampa puto")
                    continue
                break
            except:
                print("solo numros")
        return per
    
def jugando(jugador1,jugador2,juego):
    turno = 0 
    while turno < 10:
        juego.tablero()
        persona1 = jugador1.turno(juego)
        if persona1 == 2012:
            print("juego terminado")
            break
        jugador1.agregar(persona1)
        juego.modificar(persona1,"x")
        validacion = jugador1.validar()
        
        if validacion == True:
            juego.tablero()
            print("ganaste")
            break
        juego.tablero()
        persona2 = jugador2.turno(juego)
        if persona2 == 2012:
            print("juego terminado")
            break        
        jugador2.agregar(persona2)
        juego.modificar(persona2,"O")
        if validacion == True:
            juego.tablero()
            print("ganaste")
            break
        if turno == 9:
            print("enpate")
class juego:
    def iniciar(self):
        while True: 
            print("MICHI:")
            print("-iniciar")
            print("-salir")
            accion = input("que elijes: ").lower().strip()
            if accion == "salir":
                print("ok")
                break
            elif accion == "iniciar":
                nombre_del_jugador1 = input("nombre del jugador 1 : ")
                nombre_del_jugador2 = input("nombre del jugador 2 : ")
                tres_raya = michi()                
                jugador1 = jugador(nombre_del_jugador1)
                jugador2 = jugador(nombre_del_jugador2)
                
                jugando(jugador1,jugador2,tres_raya)
                continue
            else:
                print("pendejo es si o no")
                continue

                


j = juego()
j.iniciar()