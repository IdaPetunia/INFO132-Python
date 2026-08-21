#oppgave 1


import tkinter as tk


window =tk.Tk()

button = tk.Button(window, text = 'Farvel', command =window.destroy)
button.pack()


#oppgave 2

nr = 0
vindu = tk.Tk()

def count():
    global nr
    nr +=1
    knapp.config(text = nr)

knapp = tk.Button(vindu, text = 0, command = count)
knapp.pack()

vindu.mainloop()