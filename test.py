import tkinter as tk
from tkinter import messagebox

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sample Application")
        self.geometry("400x300")
        self.resizable(True, True)
app=App()
app.mainloop()

