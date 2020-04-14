# https://realpython.com/python-gui-tkinter/#getting-user-input-with-entry-widgets
import tkinter as tk

window = tk.Tk()

beschriftung = tk.Label(text='Bitte Name eingeben:')

eingabe = tk.Entry(
    fg='yellow',
    bg='blue',
    width=50
)
beschriftung.pack()
eingabe.pack()

name = eingabe.get()

window.mainloop()