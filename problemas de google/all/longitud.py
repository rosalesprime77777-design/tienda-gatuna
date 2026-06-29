matriz_correcta = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
matriz_incorrecta = [[1, 2, 3], [4, 5], [7, 8, 9]]
def verificar(lista):
    lista_verificada = all(len(num) == 3 for num in lista)
    print(lista_verificada)
    
verificar(matriz_incorrecta)