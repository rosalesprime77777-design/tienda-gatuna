import tkinter as tk

class  validar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.estado = True
        self.texto = tk.StringVar()
        self.geometry("200x300")
        self.configure(bg="#080505")
        
    def cambiar(self):
        if self.estado == True:
            self.estado = False
            self.letra.trace_remove("write",self.acosador)
        else:
            self.estado = True
            self.letra.trace_add("write",self.mayus)
            self.mayus()
            
    def mayus(self,*args):    
        variable_por_gusto = self.letra.get()
        self.texto.set(variable_por_gusto.upper())
        
    def entrada(self):
        self.letra = tk.StringVar()
        self.acosador = self.letra.trace_add("write",self.mayus)
        puerta = tk.Entry(self,textvariable=self.letra)
        puerta.pack()
            
        
    def boton(self):
        gato = tk.Button(self,text="detener",command=self.cambiar)
        gato.pack()
        
    def cartel(self):
        letrero = tk.Label(self,textvariable=self.texto)
        letrero.pack()
baco = validar()
baco.entrada()
baco.boton()
baco.cartel()
baco.mainloop()