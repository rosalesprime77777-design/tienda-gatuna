from tienda_de_gatos import producto


def pedir_info_entero(texto):
    while True:
        try:
            cuanto_agregas = int(input(texto))
            if cuanto_agregas <= 0:
                print("solo numeros enteros")
                continue
            break
        except ValueError:
            print("solo numeros")
    return cuanto_agregas
    
def pedir_info_flotante(texto):
    while True:
        try:
            cuanto_agregas = float(input(texto))
            if cuanto_agregas <= 0:
                print("solo numeros enteros")
                continue
            break
        except ValueError:
            print("solo numeros")
            
    return cuanto_agregas

def crear_contraseña():
    while True: 
        print("la contraseña debe tener 8 digitos")
        contra = input("cual sera tu contraseña: ")
        verifica = all([all(i != " " for i in contra),len(contra) >= 8])
        if verifica == True:
            break 
    return contra        

def validar_contraseña (contra_verdadera):
    for i in range(1,6):
        contra = input(f"ingresa la contraseña {i}/5 : ")
        if contra_verdadera == contra:
            return True
    return False


def modificar_almacen(tienda,persona,dueño):
    if persona == "dueño":
        while True:
            #aqui tiene q aver un for q muestre todos los productos
            nombre_del_producto = input("nombre del producto : ")
            if nombre_del_producto == "salir":
                print("ok")
                break
            elif nombre_del_producto in tienda.registro:
                cantida = pedir_info_entero(f"cuantos {nombre_del_producto} vas a agregar: ")
                tienda.almacen[nombre_del_producto].aumentar(cantida)
                tienda.guardar_registro()
                continue
        
            else:
                cantida = pedir_info_entero(f"cuantos {nombre_del_producto} vas a poner: ")
                precio = pedir_info_flotante("cual sera el precio: ")
                tienda.almacen[nombre_del_producto] = producto(nombre_del_producto,cantida,precio)
                tienda.guardar_registro()
                continue
            
            
    elif persona == "cliente":
        
        while True :#adi tambien
            print("para terminar escrive salir")
            nombre_del_producto = input("nombre del producto : ")
            if nombre_del_producto == "salir":
                print("ok")
                break
            elif nombre_del_producto in tienda.registro:
                cantida = pedir_info_entero(f"cuantos {nombre_del_producto} vas a comprar: ")
                stock =tienda.almacen[nombre_del_producto].cantidad
                if stock > cantida:
                    print("error no hay suficientestock")
                    continue
                tienda.almacen[nombre_del_producto].retirar(cantida)
                tienda.guardar_registro()
                dueño.ganar_mone(tienda.almacen[nombre_del_producto],cantida)
                dueño.registro_del_dueño()
                continue
        
            else:
                print("no existe el producto: ") 
                continue 
        

        



                