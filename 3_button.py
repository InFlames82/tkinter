# https://realpython.com/python-gui-tkinter/#displaying-clickable-buttons-with-button-widgets
import tkinter as tk

window = tk.Tk()

btn = tk.Button(
    text='Klick mich!',
    width=25,
    height=5,
    bg='blue',
    fg='yellow'
)

btn.pack()

window.mainloop()