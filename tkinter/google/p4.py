import tkinter as tk 

caja = tk.Tk()
caja.geometry("200x400")
caja.resizable(False,False)
caja.configure(bg="#2d2222")

titulo = tk.Label(caja,text="caja de cambios")
titulo.pack()

cambio = tk.Frame(caja)
cambio.pack()


num_soles = tk.DoubleVar()
soles = tk.Entry(cambio)
