from tkinter import Frame, ttk
from tkinter.ttk import LabelFrame, Button
from ttkbootstrap.constants import *
from ttkbootstrap.widgets import LabelFrame, Button, Frame

class HomeViews(Frame):
     def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        # Create a LabelFrame for page directory with ttkbootstrap styles
        self.input_frame = ttk.LabelFrame(self, text="Page Directory", bootstyle="primary")
        self.input_frame.grid(row=0, column=0, padx=20, pady=10)

        # Button for "Create Rule" page
        self.rule_page_btn = ttk.Button(
            self.input_frame, text="Create Rule", bootstyle="success-outline", width=15
        )
        self.rule_page_btn.grid(row=0, column=0, padx=10, pady=10)

        self.rule_page_btn = ttk.Button(
            self.input_frame, text="Create Rule", bootstyle="success-outline", width=15
        )
        self.rule_page_btn.grid(row=0, column=0, padx=10, pady=10)

        # Button for "Client X Rule" page
        self.clientxrule_page_btn = ttk.Button(
            self.input_frame, text="Client X Rule", bootstyle="info-outline", width=15
        )
        self.clientxrule_page_btn.grid(row=1, column=0, padx=10, pady=10)

        self.benmark_page_btn = ttk.Button(
        self.input_frame, text="Bench Mark", bootstyle="info-outline", width=15
        )
        self.benmark_page_btn.grid(row=2, column=0, padx=10, pady=10)


        self.finacial_liab_page_btn = ttk.Button(
        self.input_frame, text="Finacial Liability", bootstyle="info-outline", width=15
        )
        self.finacial_liab_page_btn.grid(row=3, column=0, padx=10, pady=10)

        
        self.Net_Expo_page_btn = ttk.Button(
        self.input_frame, text="Net Exposure", bootstyle="info-outline", width=15
        )
        self.Net_Expo_page_btn.grid(row=4, column=0, padx=10, pady=10)


        '''
        self.input_frame = LabelFrame(self,text='Page Directory',style="TFrame")
        self.input_frame.grid(row=0, column=0, padx=20, pady=10)

        self.rule_page_btn = Button(self.input_frame, text="Create Rule",  bootstyle="primary")
        self.rule_page_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")

        self.clientxrule_page_btn = Button(self.input_frame, text="Client X Rule",bootstyle="success")
        self.clientxrule_page_btn.grid(row=6, column=1, padx=0, pady=10, sticky="w")
        '''

      

