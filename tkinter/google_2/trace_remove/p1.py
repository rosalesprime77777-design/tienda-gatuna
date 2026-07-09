import tkinter as tk 
class gato(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("300x600")
        self.configure(bg="#1a0e0e")
        self.texto = tk.StringVar()
        self.acosador = self.texto.trace_add("write",self.verificador)
        
        
    def verificador(self,*args):
        if self.texto.get() == "1234":
            self.texto.trace_remove("write",self.acosador)
            self.configure(bg="#15A03D")
            
        else:
            self.configure(bg="#de281b")
        
    def entrada(self):
        puerta = tk.Entry(self,textvariable=self.texto)
        puerta.pack()
        

Ni_puta_idea = gato()
Ni_puta_idea.entrada()
Ni_puta_idea.mainloop()