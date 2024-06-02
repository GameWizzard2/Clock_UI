from tkinter import *
from tkinter.ttk import *
from time import strftime

class Clock_App:
    def __init__(self):
        self.window_title = 'Clock'

    def window(self):
        self.root = Tk()
        self.root.title(self.window_title)
    
    def label_format(self):
        self.font = ('calibri', 40, 'bold')
        self.background = 'purple'
        self.foreground = 'white'
    
    def widgets(self):
        self.label_1 = Label(self.root, 
                             font = self.font,
                             background = self.background,
                             foreground = self.foreground,
                             )
        self.label_1.pack(anchor='center')


    def time(self):
        string = strftime('%H:%M:%S %p')
        self.label_1.config(text=string)
        self.label_1.after(1000, self.time)

    def run(self):
        self.window()
        
        self.label_format()
        self.widgets()
        self.time()
        self.root.mainloop()






#lbl = Label(root, font=)

#lbl.pack(anchor="center")
#mainloop()

clock = Clock_App()
clock.run()
