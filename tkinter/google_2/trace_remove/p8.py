import tkinter as tk
class gato(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("200x200")
        self.configure(bg="#3e2a2a")
    
    def enviar(self,*args):
        texto = self.edad.get()
        if texto.isdigit():
            if int(texto) >= 18:
                self.boton1.configure(state="normal")
                
            else :
                self.boton1.configure(state="disabled")
           
        else:
            self.boton1.configure(state="disabled") 
    def terminar(self):
        self.edad.trace_remove("write",self.detener)
        
    def letrero (self,texto):
        letrero = tk.Label(text=texto)
        letrero.pack(pady=10)
        
    def entrada(self):
        self.edad = tk.StringVar()
        self.detener = self.edad.trace_add("write",self.enviar)
        entrada = tk.Entry(textvariable=self.edad)
        entrada.pack()
        
    def boton(self):
        self.boton1 = tk.Button(self,text="enviar",state="disabled")
        self.boton1.pack()
        
        
o = gato()
o.letrero("verificador inteligente")
o.entrada()
o.boton()
o.mainloop()