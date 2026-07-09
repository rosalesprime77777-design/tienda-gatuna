import tkinter as tk

espejito = tk.Tk()
espejito.geometry("200x400")
#creeando mi titulo super wai
titulo = tk.Label(espejito,text="espejito")
espejito.configure(bg="#acacbd")
titulo.pack()

#mi funcion pedora
def manipulacion(*args):
    texto = gato.get()
    print(f"el pendejo escribe {texto}")

#variable str
gato = tk.StringVar()
gato.trace_add("write",manipulacion)
   
#entrada
entrada = tk.Entry(espejito,textvariable=gato)
entrada.pack()

reflejo = tk.Label(espejito,textvariable=gato)
reflejo.pack()


espejito.mainloop()