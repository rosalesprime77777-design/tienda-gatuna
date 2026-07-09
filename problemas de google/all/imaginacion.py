inventario = [
    {"item": "Hierro", "cantidad": 5},
    {"item": "Fuego de dragón", "cantidad": 1},
    {"item": "Diamante", "cantidad": 0},  # <-- ¡Ojo aquí!
    {"item": "Madera", "cantidad": 10}
]
almacen = []
for objeto in inventario:
    verifica = objeto["cantidad"] > 0
    almacen.append(verifica)
    
verifica = all(almacen)
print(verifica)


prohibidas = ["gratis", "ganar", "dinero", "click"]
mensaje = "Hola amigo entra aquí para ganar un premio"
mensaje_limpio = []
for i in mensaje.split(" "):
    mensaje_limpio.append(i)
    
verificado = any(i in prohibidas for i in mensaje_limpio)
print(verificado)


clave_hacker = "GatitoPro777"
mayusculas = any(i.isupper() for i in clave_hacker)
minusculas = any(i.islower() for i in clave_hacker)
validar_contra = all([mayusculas,minusculas])
print(validar_contra)