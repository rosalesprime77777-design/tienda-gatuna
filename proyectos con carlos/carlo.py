import tkinter as tk

# Crea la ventana principal correctamente usando paréntesis
app = tk.Tk()

# Define el tamaño de la ventana (Anchura x Altura)
app.geometry("300x600")

# Cambia el color de fondo a negro
app.configure(background="black")

# Asigna el título a la ventana de forma directa
app.title("hola")

# Mantiene la ventana abierta y escuchando eventos
app.mainloop()