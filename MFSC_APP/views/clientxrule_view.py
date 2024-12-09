from tkinter import Frame, Label, Entry, Button, ttk

class ClientXRuleViews(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #Filed :REF_NO	CLIENT_CODE	RULE_CODE	USER_UPLOAD	UPLOAD_DATE	DELETE_FLAG

        self.input_section = ttk.LabelFrame(self,text='Client X RuleForm')
        self.input_section.grid(row=0, column=0, padx=20, pady=10)

        self.export_btn = Button(self.input_section,text="Export to csv")
        self.export_btn.grid(row=0, column=2, padx=5, pady=10,sticky="w")

        
        self.ref_no_lb = Label(self.input_section, text="REF NO")
        self.ref_no_lb.grid(row=1, column=0, padx=5, pady=10)
        self.ref_no_input = Entry(self.input_section)
        self.ref_no_input.grid(row=1, column=1, padx=5, pady=10)

        self.client_code_lb = Label(self.input_section,text="Client Code")
        self.client_code_lb.grid(row=2, column=0, padx=5, pady=10)
        self.client_code_input = Entry(self.input_section)
        self.client_code_input.grid(row=2, column=1, padx=5, pady=10)

        self.rule_code_lb = Label(self.input_section,text="Rule Code")
        self.rule_code_lb.grid(row=3, column=0, padx=5, pady=10)
        self.rule_code_input = Entry(self.input_section)
        self.rule_code_input.grid(row=3, column=1, padx=5, pady=10)

        self.delete_lb = Label(self.input_section,text="Delete")
        self.delete_lb.grid(row=4, column=0, padx=5, pady=10)
        self.delete_input = Entry(self.input_section)
        self.delete_input.grid(row=4, column=1, padx=5, pady=10)

        self.home_page_btn = Button(self.input_section, text="Back to Home")
        self.home_page_btn.grid(row=0, column=3, padx=0, pady=10, sticky="w")

        self.add_btn = Button(self.input_section, text="Add")
        self.add_btn.grid(row=5, column=3, padx=0, pady=10, sticky="w")

        self.del_btn = Button(self.input_section, text="Delete")
        self.del_btn.grid(row=5, column=4, padx=0, pady=10, sticky="w")
        
        self.edit_btn = Button(self.input_section, text="edit")
        self.edit_btn.grid(row=5, column=5, padx=0, pady=10, sticky="w")

        #scrooll 

        # Preview Section
        self.preview_section = ttk.LabelFrame(self, text="Preview")
        self.preview_section.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        # Define Columns for TreeView
        cols = ("REF_NO", "CLIENT_CODE", "RULE_CODE", "USER_UPLOAD", "UPLOAD_DATE", "DELETE_FLAG","ID")
        self.preview_tree = ttk.Treeview(
            self.preview_section, show="headings", columns=cols, height=20, 
            )
        for col in cols:
            self.preview_tree.heading(col, text=col)
            self.preview_tree.column(col, width=150 if col != "ID" else 0)  # Hide ID column
                
        # Add Scrollbar
        tree_scroll = ttk.Scrollbar(self.preview_section, orient="vertical", command=self.preview_tree.yview)
        tree_scroll.pack(side="right", fill="y")

        # Configure TreeView to work with Scrollbar
        self.preview_tree.configure(yscrollcommand=tree_scroll.set)

        # Configure Columns
        for heading in cols:
            self.preview_tree.heading(heading, text=heading)
            self.preview_tree.column(heading, width=150)

        # Pack the TreeView
        self.preview_tree.pack(fill="both", expand=True)

        # Configure Layout Weights for Resizing
        self.grid_rowconfigure(0, weight=0)
        self.grid_columnconfigure(1, weight=1)
        self.preview_section.grid_rowconfigure(0, weight=0)
        self.preview_section.grid_columnconfigure(0, weight=1)

    def populate_treeview(self, data):
        # Clear the TreeView
        for item in self.preview_tree.get_children():
            self.preview_tree.delete(item)
        # Add rows to the TreeView
        for _, row in data.iterrows():
            self.preview_tree.insert("", "end", values=row.to_list())

