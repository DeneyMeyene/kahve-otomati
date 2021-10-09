import tkinter as tk
from os import system
from tkinter import font
from tkinter.font import Font
from tkinter import Frame
from tkinter import messagebox

class back:
    def __init__(self,master = None) -> None:
        self.master = master
    
    def entVar(self):
        return self.ent.get()
    
    def btn(self):pass

    def help(self):pass

    def get(self):pass
    def set(self):pass
    def VAR(self):pass
    def use(self):pass
    def run(self):pass
    def console(self):pass

class color:
    def __init__(self,master = None) -> None:
        self.master = master
        self.color = None
        self.dict = {"bg":"blue"}
        self.colorize()
    def colorize(self):
        self.master.configure(self.dict)
    
    def labelC(self,dict):
        self.label.configure()
    
    def entryC(self,dict):
        self.ent.configure()
    
    def btn(self,dict):
        self.butn.configure()
    
    def checkC(self,dict):
        self.chc.configure()

class front:
    def __init__(self,master = None) -> None:
        self.master = master
        color(self.master)

    def entry(self):
        self.ent = tk.Entry(self.master)
        return self.ent.pack()
    
    def lbl(self,text):
        self.label = tk.Label(self.master,text=text)
        return self.label.pack()
    
    def foo(self):
        self.foo = tk.Label(self.master)
        return self.foo.pack()

    def sizeable(self,x=320,y=320):
        self.master.geometry("{}x{}".format(x,y))
        self.master.resizable(False,False)

    def check(self):
        self.chc = tk.Checkbutton(self.master)
        return self.chc.pack()

    def btn(self):
        self.butn = tk.Button(self.master,text="Onayla")
        return self.butn.pack()

class main:
    def __init__(self,master = None) -> None:
        self.master = master

if __name__ == "__main__":
    front(tk.Tk()).master.mainloop()
