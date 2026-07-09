import tkinter as tk

class contador(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("150x200")
        self.configure(bg="#221c1c")
        self.title("programa de mierda")
        self.texto = tk.StringVar()
        
    def cartel(self,texto):
        letrero = tk.Label(text=texto)
        letrero.pack(pady=10)
        
    def validar(self,*args):
        if self.contra.get() == "gato123":
            self.contra.trace_remove("write",self.detener)
            self.texto.set(f"contraseña corecta")
        else:
            self.texto.set("contraseña incorecta")
        
    def entrada(self):
        self.contra = tk.StringVar()
        self.detener = self.contra.trace_add("write",self.validar)
        entrada = tk.Entry(textvariable=self.contra)
        entrada.pack()
        
    def salida(self):
        letrero = tk.Label(textvariable=self.texto)
        letrero.pack()
        
con  = contador()
con.cartel("ingrese contraseña")
con.entrada()
con.salida()
con.mainloop()