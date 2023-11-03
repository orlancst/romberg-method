# from distutils.command.config import config
# import tkinter as tk
# from tkinter.tix import Tree
# import math
import numpy as np
# from scipy import integrate

import scipy.integrate


#np.exp(-x**2) + 1 / np.sqrt(np.pi)

#f = lambda x: x*np.sin(x)
def f(x):
    return x*np.sin(x)
a=0
b=np.pi/2
integralAntigua = scipy.integrate.romberg.Romberg(f, a, b)

valor = integralAntigua.integrate()

print(valor)


# def Trap(n, a, b):
#     h = (b - a) / n

#     Sum = 0

#     for i in range(1, n):
#         Sum = Sum + 2 * f(a + i * h)
#     Trap = (h / 2) * (f(a) + Sum + f(b))
#     return Trap

# I= np.zeros((10,10))
# ea = 100; n = 1; i = 1
# I[1, 1] = Trap(n, a, b)

# cadena = "Iterador \t Err. est \t\t Err. ver \t\t Integral\n"

# while ea > 0.01:
#     n = 2 ** 1

#     I[i+1 , 1] = Trap(n, a, b)
    
#     for k in range(2, i + 2):
#         j = 2 + i - k
#         I[j,k] = (4 ** (k - 1) * I[j+1, k - 1] - I[j, k - 1]) / (4 ** (k - 1) - 1)

#     ea = abs((I[1, i+1] - I[2, i]) / I[1, i+1]) * 100
#     et = abs((1.71828 - I[1, i+1]) / 1.7182) * 100

#     cadena = cadena + ('%f \t %f \t\t %f \t\t %f\n'% (i, ea, et, I[1,i+1]))

#     i += 1 

# print(cadena + '\n' + str(integralAntigua))

# ventana=tk.Tk()
# ventana.resizable(False, False)
# ventana.title("Método de Romberg")

# frame1 = tk.Frame(master=ventana, width=600, height=360)
# frame1.pack()

# lb1 = tk.Label(
#     master=frame1,
#     text="Método de Romberg, punto 23.10\nOrlando Castro y Juan Narváez.",
#     font=("Times New Roman", 16)
# )
# lb1.place(x=150, y=0)

# lbpr = tk.Label(
#     master=frame1,
#     text="Desarrollado en Python 3.8",
#     font=("Times New Roman", 10)
# )
# lbpr.place(x=440, y=45)

# #\u03C0 numero pi

# lb2 = tk.Label(
#     master=frame1,
#     text="Función:",
#     font=("Times New Roman", 14)
# )
# lb2.place(x=30, y=70)

# lbFuncion = tk.Label(
#     master=frame1,
#     text="x sin(x)",
#     font=("Times New Roman", 14, "italic")
# )
# lbFuncion.place(x=105, y=70)

# lbIntervalo = tk.Label(
#     master=frame1,
#     text="Intérvalos: [a= 0; b= \u03C0/2]",
#     font=("Times New Roman", 14),
# )
# lbIntervalo.place(x=180, y=70)

# lbErr = tk.Label(
#     master=frame1,
#     text="Error estimado: 0.01",
#     font=("Times New Roman", 14)
# )
# lbErr.place(x=390, y=70)

# txtResultado = tk.Text(
#     master=frame1,
#     height=12,
#     width=60,
#     font=("Consolas", 12),
    
# )
# txtResultado.insert(tk.INSERT, cadena)
# txtResultado.config(state=tk.DISABLED)
# txtResultado.place(x=30, y=110)


# ventana.mainloop()





