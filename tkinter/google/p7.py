import tkinter as tk 

class casa_de_canbio(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("contador")
        self.geometry("300x200")
        self.configure(bg="#0b0808")
        self.cuantos = tk.DoubleVar()
        self.canbio = tk.DoubleVar()
    def cambio(self,*args):
        try:
            res = self.cuantos.get() * 20
        except tk.TclError:
            res = 0
        self.canbio.set(res)  
            
        
    def entrada(self):
        self.cuantos.trace_add("write",self.cambio)
        entrada_pendeja = tk.Entry(self,textvariable=self.cuantos)
        entrada_pendeja.pack()
        
    def salida(self):
        texto = tk.Label(self,textvariable=self.canbio)
        texto.pack()
    def letrero(self,texto):
        letrerito = tk.Label(text=texto)
        letrerito.pack()
        
        
mi_gato = casa_de_canbio()
mi_gato.letrero("cambio de dolar")
mi_gato.entrada()
mi_gato.salida()
mi_gato.mainloop()