import tkinter as tk
class flecha_verde(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x600")
        self.configure(bg="#1a0e0e")  
        self.estado = True
        self.texto = tk.StringVar()

    def cambiar_estado(self):
        if self.estado == True:
            self.estado = False
            self.acosador()
        else:
            self.estado = True
            self.accion = self.letra.trace_add("write",self.acosador)
            self.texto.set(self.letra.get())
    def acosador(self,*args):
        if self.estado == False:
            self.letra.trace_remove("write",self.accion)
        else:
            self.texto.set(self.letra.get())

            
    def entrada(self):
        self.letra = tk.StringVar()
        self.accion = self.letra.trace_add("write", self.acosador)
        entra = tk.Entry(textvariable=self.letra)
        entra.pack()
        
    def bontom(self):
        bouton = tk.Button(command=self.cambiar_estado,text="presiona")
        bouton.pack()
        
    def salida(self):
        letrero = tk.Label(textvariable=self.texto)
        letrero.pack()
        
        
gato = flecha_verde()
gato.salida()
gato.entrada()
gato.bontom()
gato.mainloop()