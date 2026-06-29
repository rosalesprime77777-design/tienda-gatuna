import json

def verificar_optimizado():
    with open("cohera.json") as dato: 
        contenido = json.load(dato)
    verificado = all(coche['velocida'] >= 300 for coche in contenido.values())
    print(verificado)
    
verificar_optimizado()