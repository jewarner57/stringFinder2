import tkinter as tk
from tkinter import ttk

def submit_text():
    value = e1.get()
    print(value)

window = tk.Tk()

ttk.Style().configure('green/black.TButton', foreground='black', background='white')

tk.Label(window, text="First Name").grid(row=0)
tk.Label(window, text="Last Name").grid(row=1)

e1 = tk.Entry(window)
e2 = tk.Entry(window)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

#submit_button = ttk.Button(window, text="Submit", foreground="green", command=submit_text).grid(row=3)
button = ttk.Button(window, text='Submit and Run', command=submit_text, style='green/black.TButton').grid(row=3, column=1)
#button1 = tk.Button(window, text='hello', fg='red')

window.mainloop()