import tkinter as tk

atalanta = tk.Tk()
atalanta.geometry("200x400")
atalanta.configure(bg="#4e2727")
atalanta.resizable(False,False)
def proivir(*args):
    try:
        valor = palabra.get()
        if valor > 50:
            cartel.configure(bg="green",text=F"tu buelto es {valor -50}")
            
        else:
            cartel.configure(bg="red",text=F"te falta {50 - valor}")
            
    except ValueError:
        cartel.configure(bg="red",text=F"esto no es un numero {valor}")
        
palabra = tk.IntVar()
palabra.trace_add("write",proivir)
entrada = tk.Entry(atalanta,textvariable=palabra)
entrada.pack(pady=10)
cartel = tk.Label(atalanta,text="no escribio nada")
cartel.pack()
entrada.pack()
atalanta.mainloop()