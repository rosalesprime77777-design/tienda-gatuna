import tkinter as tk 

class contador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("contador")
        self.geometry("300x200")
        self.configure(bg="#0b0808")
        self.palabras = tk.StringVar()
        self.cuantos = tk.IntVar()
    def contando(self,*args):
        cantidad = len(self.palabras.get())
        self.cuantos.set(cantidad)
            
        
        
    def entrada(self):
        
        
        self.palabras.trace_add("write",self.contando)
        entrada_pendeja = tk.Entry(self,textvariable=self.palabras)
        entrada_pendeja.pack()
        
    def salida(self):
        texto = tk.Label(self,textvariable=self.cuantos)
        texto.pack()
    def letrero(self,texto):
        letrerito = tk.Label(text=texto)
        letrerito.pack()
        
        
gato = contador()
gato.letrero("contador chafa")
gato.entrada()
gato.letrero("palabras")
gato.salida()
gato.mainloop()