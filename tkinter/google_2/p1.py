import tkinter as tk 
class bipolar(tk.Tk):
    def __init__(self):
        super().__init__()
        self.modo = "sumar"
        self.title("bipolar")
        self.geometry("300x200")
        self.configure(bg="#0b0808")
        self.palabra = tk.StringVar()
        
    def modificar(self,*args):
        modifi = self.palabra.get().upper()
        self.palabra.set(modifi)
     
    def entrada(self):

        entra = tk.Entry(self,textvariable=self.palabra)
        self.palabra.trace_add("write",self.modificar)
        entra.pack(pady=5,padx=5)
      
      
    def salida(self):
        cartel= tk.Label(self,textvariable=self.palabra)  
        cartel.pack()
        
letrero = bipolar()
letrero.entrada()
letrero.salida()
letrero.mainloop()