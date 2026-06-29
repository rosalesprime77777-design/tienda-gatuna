class usuario_pendejo:
    def __init__(self,nombre,contraseña):
        self.nombre = nombre
        self.contraseña = contraseña
        
    def caracteres(self,contra):
        if len(contra) >= 8 :
            return True
        else:
            return False
        
        
while True:
    nombre = input("nombre : ")
    contra = input("contraseña para tu cuenta: ")
    usuario = usuario_pendejo(nombre,contra)
    validacion = usuario.caracteres(contra)
    if validacion == False :
        continue
    else :
        break
#no me gusta hacerlo basico pero supongo que solo es para aprender  como usar all
cuenta_nombre = input("nombre: ")
cuenta_contra = input("contra: ")
nombre_corecto = (cuenta_nombre == nombre)
contra_corecta = (cuenta_contra == contra)
if all([nombre_corecto,contra_corecta]):
    print("podes entrar pendejo")
    
else:
    print("gatos no me engañas puto")
