
import json

datos_cochera = {
    "auto_1": {"modelo": "Ferrari", "velocida": 340},
    "auto_2": {"modelo": "Lamborghini", "velocida": 350},
    "auto_3": {"modelo": "Tsuru Tuneado", "velocida": 120} # ¡Este hará fallar el all!
}

with open("cohera.json","w") as f:
    json.dump(datos_cochera,f,indent=4)
    
def verificar():
    datos_limpios = {}
    with open("cohera.json","r") as dato:#una pregunta el r no esta por defecto
        contenido = json.load(dato)
        
    for nombre,datos in contenido.items():
        datos_limpios[nombre] = {
            "velocida": datos['velocida'],
            "modelo": datos['modelo']
        }  
        
        
    verificado = all(dato['velocida']>300 for dato in datos_limpios.values() )
    print(f"todos los autos tienen una velocidad mayor a 300 {verificado}")
    
verificar()
        
    
    
