from tkinter import Tk
from config.styles import apply_styles
from ttkbootstrap import Style

class Root(Tk):
    def __init__(self):
        super().__init__()
        apply_styles()

        start_width = 800
        min_width = 250
        start_height = 900
        min_height = 250

        self.geometry(f"{start_width}x{start_height}")
        self.minsize(width=min_width, height=min_height)
        self.title("MFSC APP")
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        #apply_styles(self)