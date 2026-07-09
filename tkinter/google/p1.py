import tkinter as tk

atalanta = tk.Tk()
atalanta.geometry("200x400")
atalanta.configure(bg="#4e2727")
atalanta.resizable(False,False)
def cantidad(*args):
    texto = palabra.get()
    cartel.configure(text=f"caracteres: {len(texto)}")


palabra = tk.StringVar()
palabra.trace_add("write",cantidad)
entrada = tk.Entry(atalanta,textvariable=palabra)
entrada.pack(pady=10)
cartel = tk.Label(atalanta,text="caracteres= 0")
cartel.pack()
entrada.pack()




atalanta.mainloop()