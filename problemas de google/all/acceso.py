#ejer 1
alturas_carrito = [1.50, 1.42, 1.35, 1.60]
verificado = all(i>1.40 for i in alturas_carrito)
print(verificado)
#ejer 2
puntajes = [350, 1200, 450, 99999, 800]
veri = any(i>10000 for i in puntajes )
print(veri)
#ejer 3
notas = [8, 7, 0, 10, 9]
ceros = any(i <= 0 for i in notas)
mas_de_5 =all(i > 5 for i in notas)
print(ceros,mas_de_5)
 #ejer 4 
usuario = "gato_pro"
correo = "contacto@tiendagatuna.com"
clave = "michis"
numeros = "123456789"
def validar(usuario,correo,clave):
    numeros = "123456789"
    verifica_nombre = all([len(usuario) >3 ])
    verifica_correo = any(i == "@" for i in correo)
    verifica_clave = any(i == e for i in clave for e in numeros )
    print(verifica_nombre,verifica_correo,verifica_clave)
validar(usuario,correo,clave)
