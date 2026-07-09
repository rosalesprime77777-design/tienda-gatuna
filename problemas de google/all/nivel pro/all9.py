logs = [
    "INFO - User login from 182.16.4.1",
    "WARN - Database slow response",
    "INFO - User login from 192.168.1.50", # <-- IP Sospechosa
    "DEBUG - Cache cleared"
]
#esto es para practicar y verificar
numeros = [1,2,4,5,3] 
suma = sum(i for i in numeros)
print(suma)

verifica = any(i.startswith("192.168") for lista in logs for i in lista.split() )
print(verifica)

