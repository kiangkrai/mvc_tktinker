from tkinter import Frame, Label, Entry, Button, ttk


class RuleCreateViews(Frame):
           
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)

        self.input_frame = Frame(self)
        self.input_frame.grid(row=0, column=0, padx=5, pady=10,sticky="w")

        self.ref_no_lb = Label(self.input_frame, text="REF NO")
        self.ref_no_lb.grid(row=1, column=0, padx=5, pady=10)
        self.ref_no_input = Entry(self.input_frame)
        self.ref_no_input.grid(row=2, column=0, padx=5, pady=10)

        self.rule_code_lb = Label(self.input_frame, text="RULE_CODE")
        self.rule_code_lb.grid(row=3, column=0, padx=5, pady=10)
        self.rule_code_input = Entry(self.input_frame)
        self.rule_code_input.grid(row=4, column=0, padx=5, pady=10)

        self.rule_des_lb = Label(self.input_frame, text="RULE_DESCRIPTION")
        self.rule_des_lb.grid(row=3, column=1, padx=5, pady=10)
        self.rule_des_input = Entry(self.input_frame)
        self.rule_des_input.grid(row=4, column=1, padx=5, pady=10)

        self.fomula_lb = Label(self.input_frame, text="FORMULA")
        self.fomula_lb.grid(row=3, column=2, padx=5, pady=10)
        self.fomula_input = Entry(self.input_frame)
        self.fomula_input.grid(row=4, column=2, padx=5, pady=10)


        self.OPEN_PARENTHESIS_lb = Label(self.input_frame, text="OPEN_PARENTHESIS")
        self.OPEN_PARENTHESIS_lb.grid(row=5, column=0, padx=5, pady=10)
        self.OPEN_PARENTHESIS_input = Entry(self.input_frame)
        self.OPEN_PARENTHESIS_input.grid(row=6, column=0, padx=5, pady=10)

        
        self.CONDITION_lb = Label(self.input_frame, text="CONDITION")
        self.CONDITION_lb.grid(row=5, column=1, padx=5, pady=10)
        self.CONDITION_input = Entry(self.input_frame)
        self.CONDITION_input.grid(row=6, column=1, padx=5, pady=10)


        self.OPERATOR1_lb = Label(self.input_frame, text="OPERATOR1")
        self.OPERATOR1_lb.grid(row=5, column=2, padx=5, pady=10)
        self.OPERATOR1_input = Entry(self.input_frame)
        self.OPERATOR1_input.grid(row=6, column=2, padx=5, pady=10)


        self.CONDITION_VALUE_lb = Label(self.input_frame, text="CONDITION_VALUE")
        self.CONDITION_VALUE_lb.grid(row=5, column=3, padx=5, pady=10)
        self.CONDITION_VALUE_input = Entry(self.input_frame)
        self.CONDITION_VALUE_input.grid(row=6, column=3, padx=5, pady=10)

        self.AND_OR1_lb = Label(self.input_frame, text="AND_OR1")
        self.AND_OR1_lb.grid(row=5, column=4, padx=5, pady=10)
        self.AND_OR1_input = Entry(self.input_frame)
        self.AND_OR1_input.grid(row=6, column=4, padx=5, pady=10)

        self.CLOSE_PARENTHESIS_lb = Label(self.input_frame, text="CLOSE_PARENTHESIS")
        self.CLOSE_PARENTHESIS_lb.grid(row=5, column=5, padx=5, pady=10)
        self.CLOSE_PARENTHESIS_input = Entry(self.input_frame)
        self.CLOSE_PARENTHESIS_input.grid(row=6, column=5, padx=5, pady=10)


        self.AND_OR2_lb = Label(self.input_frame, text="AND_OR2")
        self.AND_OR2_lb.grid(row=7, column=0, padx=5, pady=10)
        self.AND_OR2_input = Entry(self.input_frame)
        self.AND_OR2_input.grid(row=8, column=0, padx=5, pady=10)

        self.OPERATOR2_lb = Label(self.input_frame, text="OPERATOR2")
        self.OPERATOR2_lb.grid(row=7, column=1, padx=5, pady=10)
        self.OPERATOR2_input = Entry(self.input_frame)
        self.OPERATOR2_input.grid(row=8, column=1, padx=5, pady=10)

        self.LIMIT_VALUE_lb = Label(self.input_frame, text="LIMIT_VALUE")
        self.LIMIT_VALUE_lb.grid(row=7, column=2, padx=5, pady=10)
        self.LIMIT_VALUE_input = Entry(self.input_frame)
        self.LIMIT_VALUE_input.grid(row=8, column=2, padx=5, pady=10)

        self.BENCHMARK_CODE_lb = Label(self.input_frame, text="BENCHMARK_CODE")
        self.BENCHMARK_CODE_lb.grid(row=9, column=0, padx=5, pady=10)
        self.BENCHMARK_CODE_input = Entry(self.input_frame)
        self.BENCHMARK_CODE_input.grid(row=10, column=0, padx=5, pady=10)

        self.BENCHMARK_CODE_lb = Label(self.input_frame, text="BENCHMARK_CODE")
        self.BENCHMARK_CODE_lb.grid(row=9, column=0, padx=5, pady=10)
        self.BENCHMARK_CODE_input = Entry(self.input_frame)
        self.BENCHMARK_CODE_input.grid(row=10, column=0, padx=5, pady=10)

        self.PRORATA_lb = Label(self.input_frame, text="PRORATA")
        self.PRORATA_lb.grid(row=9, column=1, padx=5, pady=10)
        self.PRORATA_input = Entry(self.input_frame)
        self.PRORATA_input.grid(row=10, column=1, padx=5, pady=10)

        self.CIS_MANAGER_lb = Label(self.input_frame, text="CIS_MANAGER")
        self.CIS_MANAGER_lb.grid(row=9, column=2, padx=5, pady=10)
        self.CIS_MANAGER_input = Entry(self.input_frame)
        self.CIS_MANAGER_input.grid(row=10, column=2, padx=5, pady=10)

        self.MKT_DERIVATIVE_lb = Label(self.input_frame, text="MKT_DERIVATIVE")
        self.MKT_DERIVATIVE_lb.grid(row=9, column=3, padx=5, pady=10)
        self.MKT_DERIVATIVE_input = Entry(self.input_frame)
        self.MKT_DERIVATIVE_input.grid(row=10, column=3, padx=5, pady=10)

        self.UNDERLYING_CODE_lb = Label(self.input_frame, text="UNDERLYING_CODE")
        self.UNDERLYING_CODE_lb.grid(row=9, column=3, padx=5, pady=10)
        self.UNDERLYING_CODE_input = Entry(self.input_frame)
        self.UNDERLYING_CODE_input.grid(row=10, column=3, padx=5, pady=10)

        self.REMARK_lb = Label(self.input_frame, text="REMARK")
        self.REMARK_lb.grid(row=11, column=0, padx=5, pady=10)
        self.REMARK_input = Entry(self.input_frame)
        self.REMARK_input.grid(row=12, column=0, padx=5, pady=10)

        self.DELETE_FLAG_lb = Label(self.input_frame, text="DELETE_FLAG")
        self.DELETE_FLAG_lb.grid(row=11, column=1, padx=5, pady=10)
        self.DELETE_FLAG_input = Entry(self.input_frame)
        self.DELETE_FLAG_input.grid(row=12, column=1, padx=5, pady=10)


        self.append_profiles_btn = Button(self.input_frame, text="Add Data")
        self.append_profiles_btn.grid(row=13, column=0, columnspan=1, padx=10, pady=10)
        
        self.edit_profiles_btn = Button(self.input_frame, text="Edit Data")
        self.edit_profiles_btn.grid(row=13, column=1, columnspan=1, padx=10, pady=10)

        self.del_profiles_btn = Button(self.input_frame, text="Delete Data")
        self.del_profiles_btn.grid(row=13, column=4, columnspan=1, padx=10, pady=10)

        self.home_page_btn = Button(self.input_frame, text="Back to Home")
        self.home_page_btn.grid(row=14, column=0, padx=0, pady=10, sticky="w")



        self.preview_frame = Frame(self,width=400)
        self.preview_frame.grid(row=0, column=1,padx=10,pady=10,sticky="nsew")

        cols = ('REF_NO', 'RULE_CODE', 'RULE_DESCRIPTION', 'FORMULA', 'OPEN_PARENTHESIS',
                    'CONDITION', 'OPERATOR1', 'CONDITION_VALUE', 'AND_OR1', 'CLOSE_PARENTHESIS',
                    'AND_OR2', 'OPERATOR2', 'LIMIT_VALUE', 'BENCHMARK_CODE', 'PRORATA', 'CIS_MANAGER',
                    'MKT_DERIVATIVE', 'UNDERLYING_CODE', 'REMARK', 'DELETE_FLAG', 'USER_UPLOAD', 'UPLOAD_DATE')
        
        self.preview_box = ttk.Treeview(self.preview_frame,
                                        show='headings',
                                        columns=cols,
                                        height=10,
                                        )
        
        for heading in cols:
            self.preview_box.heading(heading, text=heading)
            self.preview_box.column(heading,width=150)

        preview_scroll = ttk.Scrollbar(self.preview_frame, orient="horizontal",command=self.preview_box.xview)
        preview_scroll.pack(side="top",fill='x')
        
        self.preview_box.configure(xscrollcommand=preview_scroll.set)

        self.preview_box.pack(fill="both", expand=True)

        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=0)
        self.preview_frame.grid_rowconfigure(0, weight=0)
        self.preview_frame.grid_columnconfigure(0, weight=0)

        style = ttk.Style()
        style.configure("Treeview", rowheight=10)  # Adjust row height
        style.configure("Treeview.Heading", font=("Arial", 9))  # Header style
        style.configure("Treeview", font=("Arial", 7))  # Row font
   
    def populate_treeview(self, data):
        # Clear the TreeView
        for item in self.preview_box.get_children():
            self.preview_box.delete(item)
        # Add rows to the TreeView
        for _, row in data.iterrows():
            self.preview_box.insert("", "end", values=row.to_list())

