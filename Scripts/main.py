from tkinter import *
from tkinter.ttk import *
from time import strftime
from Settings.config import Config

class Clock_App:
    """
    A simple clock application that displays the current time
    in a formatted label using Tkinter.
    """
    def __init__(self):
        """
        Initialize the ClockApp with settings from the provided config class.
        """
        self.window_title = Config.WINDOW_TITLE
        self.label_font = Config.LABEL_FONT
        self.label_background = Config.LABEL_BACKGROUND
        self.label_foreground = Config.LABEL_FOREGROUND 

    def window(self):
        """
        Initialize the main application window and set its title.
        """
        self.root = Tk()
        self.root.title(self.window_title)
    

    def widgets(self):
        """
        Create and pack the label widget with the specified font, background, and foreground colors.
        """
        self.label_1 = Label(self.root, 
                             font = self.label_font,
                             background = self.label_background,
                             foreground = self.label_foreground,
                             )
        self.label_1.pack(anchor='center')


    def update_time(self):
        """
        Update the label with the current time every second.
        """
        string = strftime('%H:%M:%S %p')
        self.label_1.config(text=string)
        self.label_1.after(1000, self.update_time)

    def run(self):
        """
        Run the clock application by initializing the window,
        creating widgets, starting the time update loop, and running the main loop.
        """
        self.window()
        self.widgets()
        self.update_time()
        self.root.mainloop()


clock = Clock_App()
clock.run()
