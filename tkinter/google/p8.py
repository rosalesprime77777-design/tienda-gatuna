import tkinter as tk 
class bipolar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.modo = "sumar"
        self.title("bipolar")
        self.geometry("300x200")
        self.configure(bg="#0b0808")
        
        self.valores = []
        self.num1 = tk.DoubleVar()
        self.cartel = tk.Frame()
        self.cartel.pack()
        self.respuesta = tk.DoubleVar()
    def cambio(self):
        if self.modo == "sumar":
            self.modo = "multiplicar"
        else:
            self.modo = "sumar"
            
        self.operaciones()
    def operaciones(self,*args):
        try:
            if len(self.valores) < 2:
                return
            elif self.modo == "sumar":
                res = sum(i.get() for i in self.valores) 
            
            else:
                res = self.valores[0].get() * self.valores[1].get()
            
            self.respuesta.set(res)
                
        except (tk.TclError,IndexError):
            self.respuesta.set(0)
        
    def boton(self):
        canbio = tk.Button(self,text="cambio",command=self.cambio)
        canbio.pack()
        
    def entrada(self,fila,columna):
        valor = tk.DoubleVar()
        valor.trace_add("write",self.operaciones)
        self.valores.append(valor)
        entra = tk.Entry(self.cartel,textvariable=valor)
        entra.grid(row=fila,column=columna,pady=5,padx=5)
      
      
    def salida(self):
        cartel= tk.Label(self,textvariable=self.respuesta)  
        cartel.pack()
        
canbio = bipolar()
canbio.entrada(0,0)
canbio.entrada(0,1)
canbio.boton()
canbio.salida()
canbio.mainloop()