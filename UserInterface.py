import tkinter as tk
from tkinter import ttk
from functools import partial

class UserInterface:

    def __init__(self):
        self.directoryPath = ""
        self.searchString = ""
        self.outputOrder = ""
        self.window = tk.Tk()

    #called when submit button is pressed
    #e1, e2, e3 are the three text inputs
    def submit_form_text(self, e1, e2, e3):
        self.directoryPath = e1.get()
        self.searchString = e2.get()
        self.outputOrder = e3.get()
        self.window.destroy()

    def createTkWindow(self):

        #create a ttk style to make the button text black
        ttk.Style().configure('black.TButton', foreground='black', background='white')

        #create labels for spacing and displaying input names
        tk.Label(self.window, text="File Path To Directory").grid(row=0)
        tk.Label(self.window, text="").grid(row=1)
        tk.Label(self.window, text="Search String").grid(row=2)
        tk.Label(self.window, text="").grid(row=3)
        tk.Label(self.window, text="Output Order").grid(row=4)
        tk.Label(self.window, text="").grid(row=5)

        #create three text inputs
        e1 = tk.Entry(self.window)
        e2 = tk.Entry(self.window)
        e3 = tk.Entry(self.window)

        #position the text inputs
        e1.grid(row=0, column=1)
        e2.grid(row=2, column=1)
        e3.grid(row=4, column=1)

        #create a submit button
        button = ttk.Button(self.window, text='Submit and Run', command=partial(self.submit_form_text, e1, e2, e3), style='black.TButton').grid(row=6, column=1)

        self.window.mainloop()

    def getTerminalInput(self):
        self.directoryPath = input("Please enter the absolute path to the directory you would like to search: ")
        self.searchString = input("Please enter your search string: ")
        self.outputOrder = input("Please enter the order you would like the output to be in: ")
    