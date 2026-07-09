import tkinter as tk

atalanta = tk.Tk()
atalanta.geometry("200x400")
atalanta.configure(bg="#4e2727")
atalanta.resizable(False,False)
def proivir(*args):
    texto_prohibido = ["puto"]#solo pongo eso da pereca aser mas 
    texto = palabra.get()
    verificar = any(i in texto_prohibido for i in texto.split())
    if verificar == True:
        cartel.configure(bg="red",text="se detecto una \n palabra proibida")
    else:
        cartel.configure(bg="green",text=texto)

palabra = tk.StringVar()
palabra.trace_add("write",proivir)
entrada = tk.Entry(atalanta,textvariable=palabra)
entrada.pack(pady=10)
cartel = tk.Label(atalanta,text="no escribio nada")
cartel.pack()
entrada.pack()
atalanta.mainloop()