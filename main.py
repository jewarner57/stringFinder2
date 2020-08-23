import tkinter as tk
from tkinter import ttk
from functools import partial

directoryPath = ""
searchString = ""
outputOrder = ""

def submit_form_text(e1, e2, e3):
    directoryPath = e1.get()
    searchString = e2.get()
    outputOrder = e3.get()

def createTkWindow():
    window = tk.Tk()

    ttk.Style().configure('green/black.TButton', foreground='black', background='white')

    tk.Label(window, text="File Path To Directory").grid(row=0)
    tk.Label(window, text="").grid(row=1)
    tk.Label(window, text="Search String").grid(row=2)
    tk.Label(window, text="").grid(row=3)
    tk.Label(window, text="Output Order").grid(row=4)
    tk.Label(window, text="").grid(row=5)

    e1 = tk.Entry(window)
    e2 = tk.Entry(window)
    e3 = tk.Entry(window)


    e1.grid(row=0, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=4, column=1)

    #submit_button = ttk.Button(window, text="Submit", foreground="green", command=submit_text).grid(row=3)
    button = ttk.Button(window, text='Submit and Run', command=partial(submit_form_text, e1, e2, e3), style='green/black.TButton').grid(row=6, column=1)
    #button1 = tk.Button(window, text='hello', fg='red')

    window.mainloop()

def getTerminalInput():
    directoryPath = input("Please enter the absolute path to the directory you would like to search: ")
    searchString = input("Please enter your search string: ")
    outputOrder = input("Please enter the order you would like the output to be in: ")
    

try:
    createTkWindow()
except:
    print("Interface window Could not be opened... Defaulting to text")
    getTerminalInput()
