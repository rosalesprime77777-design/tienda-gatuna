import tkinter as tk

idea = tk.Tk()
idea.geometry("200x400")
idea.configure(bg="#415681")



def saludar(*args):
    variable = valor_str.get()
    letrero_actualisado.configure(text=f"hola {variable}")
    


valor_str = tk.StringVar()
valor_str.trace_add("write",saludar)

entrada = tk.Entry(idea,textvariable=valor_str)
entrada.pack()

letrero_actualisado = tk.Label(idea,text="hola")
letrero_actualisado.pack()
idea.mainloop()
