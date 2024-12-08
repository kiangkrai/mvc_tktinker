from tkinter import Frame, Label, Entry, Button, ttk

class HomeViews(Frame):
     def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.input_frame = ttk.Labelframe(self,text='Page Directory')
        self.input_frame.grid(row=0, column=0, padx=20, pady=10)

        self.rule_page_btn = Button(self.input_frame, text="Create Rule")
        self.rule_page_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")

        self.clientxrule_page_btn = Button(self.input_frame, text="Client X Rule")
        self.clientxrule_page_btn.grid(row=6, column=1, padx=0, pady=10, sticky="w")


      

