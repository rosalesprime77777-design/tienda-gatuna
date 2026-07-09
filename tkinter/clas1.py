import tkinter as tk

app = tk.Tk()
app.title("la tienda del gato")
#ancho/alto
app.geometry("300x600")
#ancho/largo
app.resizable(False,True)#esta mierda sirve para q no se mueva la pendejada
app.configure(bg="#3e3e46")
titulo_pendejo= tk.Label(
    app,
    text="ingrese su nombre",
    pady=10,
    padx=10,
    font=("Arial",14,"bold"),
    #alto del letrero
    height=1,
    #anchor sirve para acomodar las malditas letras
    anchor="center" 
    )
titulo_pendejo.pack(pady=(10,0))#algo de ingles left = isquierda y right = derecha
#app.after(20000,"los gatos son dioses")

def saludar():
    nombre = entrada.get()
    #letrero_pendejo.configure(text=f"hola {nombre}")
    valor_strign.set(f"hola {nombre}")

entrada= tk.Entry(app,)
entrada.pack(pady=20)
valor_strign = tk.StringVar()
valor_strign.set("esperando q el idiota..........")

boton = tk.Button(
    app,
    text="preciona",
    font=("Arial",18,"bold"),
    cursor="hand2",
    command=saludar
    )
boton.pack(pady=15)

letrero_pendejo = tk.Label(app,font=("Arial",14),textvariable=valor_strign)
letrero_pendejo.pack()
app.mainloop()