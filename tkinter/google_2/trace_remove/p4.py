import tkinter as tk

class contador(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("150x200")
        self.configure(bg="#221c1c")
        self.title("programa de mierda")
        self.texto = tk.StringVar()
        
    def contar(self,*args):
        if len(self.gato.get()) == 0:
            self.texto.set("no hay palabras")
        
        elif len(self.gato.get()) > 20:
            texto_importante = self.gato.get()[:20]
            self.gato.trace_remove("write",self.vigilante)
            self.gato.set(texto_importante)
            self.texto.set("ya son 20 palabras")
            
        else:
            self.texto.set(f"palabras {len(self.gato.get())}/20")
        
    def entrada(self):
        self.gato = tk.StringVar()
        self.vigilante = self.gato.trace_add("write",self.contar)
        puerta = tk.Entry(self,textvariable=self.gato)
        puerta.pack()
        
    def salida(self):
        letrero = tk.Label(self,textvariable=self.texto)
        letrero.pack()
        
gato = contador()
gato.entrada()
gato.salida()
gato.mainloop()