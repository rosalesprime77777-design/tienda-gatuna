import tkinter as tk   
class gato(tk.Tk):
    def __init__ (self):
        super().__init__()
        self.geometry("200x300")
        self.configure(bg="#17ce1d")
        
    def amarillo(self,*args):
        self.configure(bg="#e8bd15")
        
    def fijar(self):
        self.letra.trace_remove("write",self.detener)
        self.configure(bg="#f31e1e")

    def entrada(self):
        self.letra = tk.StringVar()
        self.detener= self.letra.trace_add("write",self.amarillo)
        entrada = tk.Entry(textvariable=self.letra)
        entrada.pack()
        
    def boton(self):
        boton = tk.Button(command=self.fijar,text="fijar")
        boton.pack()
        
        
ga = gato()
ga.entrada()
ga.boton()
ga.mainloop()