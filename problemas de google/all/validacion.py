numeros_1 = [2, 4, 6, 8, 10]
numeros_2 = [2, 3, 6, 8, 10] 
def todo_par(lista):
    vererificado = all(num %2 == 0 for num in lista)
    print(vererificado)
    
todo_par(numeros_2)