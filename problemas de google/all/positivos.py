matriz_positiva = [[1, 2], [3, 4, 5]]
matriz_con_negativo = [[1, -2], [3, 4, 5]]
def positivo(lista):
    verificado = all(i > 0 for num in lista  for i in num )
    print(verificado)
    
positivo(matriz_positiva)