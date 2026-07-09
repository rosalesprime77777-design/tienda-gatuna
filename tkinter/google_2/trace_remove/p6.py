import tkinter as tk

class contador(tk.Tk):
    def __init__(self,):
        super().__init__()
        self.geometry("150x200")
        self.configure(bg="#221c1c")
        self.title("programa de mierda")
        self.texto = tk.StringVar()
        self.verificado = tk.BooleanVar()
    def cartel(self,texto):
        letrero = tk.Label(text=texto)
        letrero.pack(pady=10)
        
    def flecha(self,*args): 
        print(self.palabrosa.get())  
        
        
    def verificar(self):
        if self.verificado.get() == True:
            self.detener = self.palabrosa.trace_add("write",self.flecha)
            print("esta activad0")
        else :
            self.palabrosa.trace_remove("write",self.detener)
            print("el pendejo lo desactibo")
    def entrada(self):
        self.palabrosa = tk.StringVar()
        entrada = tk.Entry(textvariable=self.palabrosa)
        entrada.pack()
        
    def boton(self):
        boton = tk.Checkbutton(
            text="hola",
            variable=self.verificado,
            command= self.verificar
            )
        boton.pack()
        
c = contador()
c.cartel("soy un genio de la pregramacion")#lo dije cuando pense q lo abia resulto asta q bi el bug y esto se bolovio ironico
c.boton()
c.entrada()
c.mainloop()