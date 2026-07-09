import tkinter as tk
calculadora = tk.Tk()
calculadora.geometry("200x400")
calculadora.configure(bg="#3e3e46")

titulo = tk.Label(
    calculadora,
    text="ingrese los numeros\n para sumarlos ",
    font=("Arial",14)
    )

titulo.pack(pady=10)

calcu_pantalla = tk.Frame(calculadora)
valor1 = tk.IntVar()
num1 = tk.Entry(calcu_pantalla,width=4,textvariable=valor1)
num1.pack(side="right",padx=10,pady=10,)

valor2 = tk.IntVar()
num2 = tk.Entry(calcu_pantalla,width=4,textvariable=valor2)
num2.pack(side="left",padx=10,pady=10)



calcu_pantalla.pack(pady=10)
def sumando():
    try:
        respuesta = valor2.get() + valor1.get()
        resultado.configure(text=respuesta)
    except:
        resultado.configure(text="error")
def restar():
    try:
        respuesta = valor2.get() - valor1.get()
        resultado.configure(text=respuesta)
    except:
        resultado.configure(text="error")
        
def multiplicar():
    try:
        respuesta = valor2.get() * valor1.get()
        resultado.configure(text=respuesta)
    except:
        resultado.configure(text="error")
def dividir():
    try:
        respuesta = valor2.get() / valor1.get()
        resultado.configure(text=respuesta)
    except:
        resultado.configure(text="error")
        
caja_de_botones = tk.Frame(calculadora,pady=10,padx=10)      
caja_de_botones.pack(pady=10)

p1 = tk.Button(caja_de_botones,text="sumar",font=("Arial",14),command=sumando)
p1.grid(pady=5,padx=5,row=0,column=0)

p2 = tk.Button(caja_de_botones,text="dividir",font=("Arial",14),command=dividir)
p2.grid(pady=5,padx=5,row=0,column=1)

p3 = tk.Button(caja_de_botones,text="restar",font=("Arial",14),command=restar)
p3.grid(pady=5,padx=5,row=1,column=0)

p4 = tk.Button(caja_de_botones,text="mutiplicar",font=("Arial",14),command=multiplicar)
p4.grid(pady=5,padx=5,row=1,column=1)

resultado = tk.Label(calculadora,text="no as echo nada")
resultado.pack()
calculadora.mainloop()