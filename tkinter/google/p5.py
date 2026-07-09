import tkinter as tk
class app(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("calculadora")
        self.geometry("200x400")
        self.configure(bg="#625252")
        self.resizable(False,False)
        self.titulo("calculadora")
        self.cartel = tk.Frame(self,bg="#221A1A")
        self.valores = []
        self.resultado = tk.IntVar()
        self.cartel.pack()
        
    def titulo(self,titulo):
        cartel = tk.Label(self,text=titulo,font=("Arial",14,"bold"),)
        cartel.pack(pady=10)
    
    
    def suma(self,*args):
        try:
            resultado1 = sum(a.get() for a in self.valores)
            
        except tk.TclError:
            resultado1 = 0
        self.resultado.set(resultado1)
    def entrada(self,filas,columnas):
        numero = tk.IntVar()
        numero.trace_add("write",self.suma)
        self.valores.append(numero)
        entra = tk.Entry(self.cartel,width=4,textvariable=numero)
        entra.grid(pady=10,padx=5,row=filas,column=columnas,)
        
    def salida(self):
        letrero = tk.Label(textvariable=self.resultado)
        letrero.pack(pady=10)
        
    
    
api = app()
api.titulo("sumas")
api.entrada(0,0)
api.entrada(0,1)
api.salida()
api.mainloop()