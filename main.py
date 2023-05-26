import tkinter as tk
window = tk.Tk()
z = 0
mess = tk.StringVar()
mess2 = tk.StringVar()
window.geometry('150x150')
e1 = tk.Entry(textvariable= mess)
e1.pack()
e2 = tk.Entry(textvariable= mess2)
e2.pack()
l1 = tk.Label(font = 'Arial', padx = 6, pady = 6,)

l1.pack()
def modal():
    a = int(e1.get())
    b = int(e2.get())
    z = a*a + b*b
    l1.config(text = f'√{z}')

b1 = tk.Button(text = 'Modal', command=modal)
b1.pack()
window.mainloop()

