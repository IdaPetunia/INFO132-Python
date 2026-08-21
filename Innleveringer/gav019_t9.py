#oppgave 1


import tkinter as tk
from tkinter import *



window =tk.Tk()

button = tk.Button(window, text = 'Farvel', command =window.destroy)
button.pack()


#oppgave 2

nr = 0
vindu = tk.Tk()

def count():
    global nr

    nr +=1
    counter.config(text = nr)


counter = Label(vindu, text = count)
knapp = tk.Button(vindu, text = '+1', command = count)
knapp.pack()
counter.pack()


vindu.mainloop()
