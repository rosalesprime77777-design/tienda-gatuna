import tkinter as tk
class gato(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("200x200")
        self.configure(bg="#3e2a2a")
        self.intentos = 0
        self.texto= tk.StringVar()
        self.texto.set("ingrese su contraseña")
        
    def bloqueo(self,*args):
        if self.intentos >= 3:
            self.contraseña.trace_remove("write",self.detener)
            self.entrada.configure(state="disabled")
            self.boton.configure(state="disabled")
            self.texto.set("llama al banco imbecil")
          
    def validar(self):
        contra = self.contraseña.get()
        if contra == "1234":
            self.texto.set("contraseña corecta")
            self.boton.configure(state="disabled")
            self.entrada.configure(state="disabled")
            
        else:
            self.intentos += 1
            self.texto.set("contra incorrecta")
            self.bloqueo()
        
        
    def entrada1(self):
        self.contraseña = tk.StringVar()
        self.detener = self.contraseña.trace_add("write",self.bloqueo)
        self.entrada = tk.Entry(self,textvariable=self.contraseña)
        self.entrada.pack()
        
    def boton1(self):
        self.boton =tk.Button(self,command=self.validar,text="enviar")
        self.boton.pack()
        
    def salida(self):
        letrero = tk.Label(self, textvariable=self.texto, bg="#3e2a2a", fg="white", font=("Arial", 11, "bold"))
        letrero.pack(pady=20)
        
        
cajero = gato()
cajero.entrada1()
cajero.boton1()
cajero.salida()
cajero.mainloop()
