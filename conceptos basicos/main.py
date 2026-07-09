import tkinter as tk
ventana = tk.Tk()
ventana.title("vete a la mierda")
ventana.geometry("300x600")
ventana.resizable(False,False)
ventana.configure(bg="#26262b")
def saluda():
    nombre = entrada_de_texto.get().strip()
    tk.Label(ventana,
             text= f"te llamas {nombre}",
             width=15,
             height=4
             ).pack(pady=10)

cartel = tk.Label(
    ventana,text="ostias vete a la mierda",
    width=18,#llargo
    height=2,#alto
    font=("Arial", 15, "bold"),
    bg="#3e3e46",
    fg= "#9f9faa",
    padx=4,#pone releno a los costados
    pady=10 #pne relleno ariba abajo
    )
cartel.pack(
    fill= "x",
    pady= (20,0),#marca los contornos de ariva y abajo
    padx=(15,15),#marac los contornos de los costados
)
contenedor_de_botones = tk.Frame(ventana,bg= "#4F4F57",pady= 10)
contenedor_de_botones.pack(
    pady= (15,0),
    )


boton1 = tk.Button(
    contenedor_de_botones,
    text="saludando a una puta",
    width= 15,
    height= 3,
    command=saluda
    
    
)
boton1.pack(
    side = "left",
    padx= 10,
)

boton2 = tk.Button(
    contenedor_de_botones,
    text="preciona mierda",
    width= 15,
    height= 3,
    
    
)
boton2.pack(
    side = "left",
    padx= 10,

)

entrada_de_texto = tk.Entry(
    ventana,
)
entrada_de_texto.pack(pady=(10,0))

tk.mainloop()