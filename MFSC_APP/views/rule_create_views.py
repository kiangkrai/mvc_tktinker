from tkinter import Frame, Label, Entry, Button, ttk

class RuleCreateViews(Frame):
     def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        

        self.input_frame = ttk.Labelframe(self,text='input box')
        self.input_frame.grid(row=0, column=0, padx=20, pady=10)

        self.header = Label(self.input_frame, text="Please Input Client Profiles")
        self.header.grid(row=0, column=0, columnspan=1, padx=10, pady=10)


        self.input_data = Entry(self.input_frame)
        self.input_data.grid(row=1, column=0, padx=5, pady=10)
        
        self.append_profiles_btn = Button(self.input_frame, text="Add Data")
        self.append_profiles_btn.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
        
        self.edit_profiles_btn = Button(self.input_frame, text="Edit Data")
        self.edit_profiles_btn.grid(row=2, column=1, columnspan=1, padx=10, pady=10)

        self.del_profiles_btn = Button(self.input_frame, text="Delete Data")
        self.del_profiles_btn.grid(row=2, column=2, columnspan=1, padx=10, pady=10)

        self.home_page_btn = Button(self.input_frame, text="Back to Home")
        self.home_page_btn.grid(row=5, column=1, padx=0, pady=10, sticky="w")



        self.preview_frame = Frame(self)
        self.preview_frame.grid(row=0, column=1,pady=10)
        self.preview_scroll = ttk.Scrollbar(self.preview_frame)
        self.preview_scroll.pack(side='right',fill='x')


        
        cols = ('REF_NO', 'RULE_CODE', 'RULE_DESCRIPTION', 'FORMULA', 'OPEN_PARENTHESIS',
                    'CONDITION', 'OPERATOR1', 'CONDITION_VALUE', 'AND_OR1', 'CLOSE_PARENTHESIS',
                    'AND_OR2', 'OPERATOR2', 'LIMIT_VALUE', 'BENCHMARK_CODE', 'PRORATA', 'CIS_MANAGER',
                    'MKT_DERIVATIVE', 'UNDERLYING_CODE', 'REMARK', 'DELETE_FLAG', 'USER_UPLOAD', 'UPLOAD_DATE')
        
        self.preview_box = ttk.Treeview(self.preview_frame,show='headings',
                                        xscrollcommand=self.preview_scroll.set,columns=cols,height=13)
        
        for heading in cols:
            self.preview_box.heading(heading, text=heading)
            self.preview_box.column(heading,width=100)
     
        '''   
        self.preview_box.column("Name", width=100) 
        self.preview_box.column("Age", width=50)
        self.preview_box.column("Subscription", width=100)
        self.preview_box.column("Employment", width=100)
        '''
     
        self.preview_box.pack()
        
        self.preview_scroll.config(command=self.preview_box.xview)


