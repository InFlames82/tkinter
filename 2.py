import tkinter as tk



window = tk.Tk()
label = tk.Label(
    text = "Hello, Tkinter",
    foreground='white',
    background='black',
    width=10,
    height=5
)

label.pack()

window.mainloop()