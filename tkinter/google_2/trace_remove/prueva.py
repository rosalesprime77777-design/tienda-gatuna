import tkinter as tk

class contador(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("250x300")
        self.configure(bg="#221c1c")
        self.title("Programa de un Genio")
        self.verificado = tk.BooleanVar()
        
    def cartel(self, texto):
        letrero = tk.Label(self, text=texto, bg="#221c1c", fg="white")
        letrero.pack(pady=10)
        
    # 1. EL VIGILANTE: Solo se encarga de imprimir en consola cuando escribes
    def vigilante_imprimir(self, *args):
        print(self.palabrosa.get())
        
    # 2. EL INTERRUPTOR: Es llamado por el Checkbutton y controla el cable
    def controlar_alarma(self):
        if self.verificado.get() == True:
            # Si el usuario marca la casilla, CONECTAMOS el cable y guardamos el ID
            self.detener = self.palabrosa.trace_add("write", self.vigilante_imprimir)
            print("--- Vigilancia ACTIVADA ---")
        else:
            # Si el usuario desmarca la casilla, SEPARAMOS el cable usando el ID
            self.palabrosa.trace_remove("write", self.detener)
            print("--- El usuario la desactivó (Vigilancia APAGADA) ---")

    def entrada(self):
        self.palabrosa = tk.StringVar()
        # Nota: Al principio el programa empieza con el cable desconectado 
        # hasta que el usuario marque la casilla por primera vez.
        entrada = tk.Entry(self, textvariable=self.palabrosa)
        entrada.pack(pady=10)
        
    def boton(self):
        # El botón ahora llama a 'controlar_alarma' (el interruptor), no al vigilante
        boton = tk.Checkbutton(
            self,
            text="Activar Vigilancia en Consola",
            variable=self.verificado,
            command=self.controlar_alarma,
            bg="#221c1c",
            fg="black"
        )
        boton.pack(pady=10)
        
c = contador()
c.cartel("¿Soy un genio de la programación?") 
c.boton()
c.entrada()
c.mainloop()