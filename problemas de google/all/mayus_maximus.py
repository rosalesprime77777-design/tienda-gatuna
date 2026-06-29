mensajes_gritos = [["HOLA", "QUE"], ["TAL", "BIEN"]]
mensajes_mixtos = [["HOLA", "que"], ["TAL", "BIEN"]]

def grito_de_goku(lista):
    verificar = all(i.isupper() for letra in lista  for i in letra)
    print(verificar)
    
grito_de_goku(mensajes_mixtos)