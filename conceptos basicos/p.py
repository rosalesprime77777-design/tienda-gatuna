import tkinter as tk

tienda = tk.Tk()
tienda.geometry("250x500")
tienda.configure(bg="#26262b")
tienda.resizable(False,False)
titulo = tk.Label(
    tienda,
    text= "tienda don gato",
    font= ("Arial", 15, "bold"),
    pady= 10,
    padx= 5,
    bg="#84848f"
)
titulo.pack(
    pady= 10,
    padx= 5
)
def saludar():
    cartel.configure(text= "hi puto")
caja_de_botones = tk.Frame(tienda,bg="#44445f",pady=10)
caja_de_botones.pack()
boton1 = tk.Button(caja_de_botones,text="presioname\nputo",command=saludar, cursor="hand2")
boton1.pack(    side = "left",
    padx= 10,)

def eliminar():
    cartel.configure(text=" ")


boton2 = tk.Button(caja_de_botones,text="borar puto",command=eliminar,cursor="heart")
boton2.pack(    side = "left",
    padx= 10,)

cartel= tk.Label(tienda,width=18,height=1,font=("Arial", 15, "bold"))
cartel.pack(pady=100)
tienda.mainloop()