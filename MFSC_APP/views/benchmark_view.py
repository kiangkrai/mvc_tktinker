from tkinter import Frame, Label, Entry, Button, ttk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re



class BenchmarkView(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #Filed :REF_NO	CLIENT_CODE	RULE_CODE	USER_UPLOAD	UPLOAD_DATE	DELETE_FLAG

      

        self.input_section = ttk.LabelFrame(self,text='')
        self.input_section.grid(row=0, column=0, padx=20, pady=10)

        self.export_btn = ttk.Button(self.input_section,text="Export to csv")
        self.export_btn.grid(row=0, column=2, padx=5, pady=10,sticky="w")

       
        self.ref_no_lb = ttk.Label(self.input_section, text="REF NO")
        self.ref_no_lb.grid(row=1, column=0, padx=5, pady=10)
        self.ref_no_input = ttk.Entry(self.input_section)
        self.ref_no_input.grid(row=1, column=1, padx=5, pady=10)

        self.effect_dt_lb = ttk.Label(self.input_section,text="EFFECTIVE_DATE")
        self.effect_dt_lb.grid(row=2, column=0, padx=5, pady=10)
        self.effect_dt_input = ttk.Entry(self.input_section)
        self.effect_dt_input.grid(row=2, column=1, padx=5, pady=10)

        self.BEN_CODE_lb = ttk.Label(self.input_section,text="BEN_CODE")
        self.BEN_CODE_lb.grid(row=3, column=0, padx=5, pady=10)
        self.BEN_CODE_input = ttk.Entry(self.input_section)
        self.BEN_CODE_input.grid(row=3, column=1, padx=5, pady=10)
        self.BEN_CODE_input.bind("<KeyRelease>", self.validate_ben_code)

        self.BEN_DESC_lb = ttk.Label(self.input_section,text="BEN_DESC")
        self.BEN_DESC_lb.grid(row=4, column=0, padx=5, pady=10)
        self.BEN_DESC_input = ttk.Entry(self.input_section)
        self.BEN_DESC_input.grid(row=4, column=1, padx=5, pady=10)
        self.BEN_DESC_input.bind("<KeyRelease>", self.validate_ben_des_code)

        self.SEC_CODE_lb = ttk.Label(self.input_section,text="SEC_CODE")
        self.SEC_CODE_lb.grid(row=5, column=0, padx=5, pady=10)
        self.SEC_CODE_input = ttk.Entry(self.input_section)
        self.SEC_CODE_input.grid(row=5, column=1, padx=5, pady=10)
        self.SEC_CODE_input.bind("<KeyRelease>", self.validate_sec_code)



        self.SEC_TYPE_lb = ttk.Label(self.input_section,text="SEC_TYPE")
        self.SEC_TYPE_lb.grid(row=6, column=0, padx=5, pady=10)
        self.SEC_TYPE_input = ttk.Entry(self.input_section)
        self.SEC_TYPE_input.grid(row=6, column=1, padx=5, pady=10)
        self.SEC_TYPE_input.bind("<KeyRelease>", self.validate_sec_type)


        self.PER_WEIGHT_lb = ttk.Label(self.input_section,text="PER_WEIGHT")
        self.PER_WEIGHT_lb.grid(row=7, column=0, padx=5, pady=10)
        self.PER_WEIGHT_input = ttk.Entry(self.input_section)
        self.PER_WEIGHT_input.grid(row=7, column=1, padx=5, pady=10)
        self.PER_WEIGHT_input.bind("<KeyRelease>", self.validate_per_weight)


        self.DELETE_FLAG_lb = ttk.Label(self.input_section,text="DELETE_FLAG")
        self.DELETE_FLAG_lb.grid(row=8, column=0, padx=5, pady=10)
        self.DELETE_FLAG_input = ttk.Combobox(self.input_section, values=["DELETE"],state="readonly")
        self.DELETE_FLAG_input.grid(row=8, column=1, padx=5, pady=10)


        self.home_page_btn = ttk.Button(self.input_section, text="Back to Home")
        self.home_page_btn.grid(row=0, column=3, padx=0, pady=10, sticky="w")

        self.add_btn = ttk.Button(self.input_section, text="Add")
        self.add_btn.grid(row=5, column=3, padx=0, pady=10, sticky="w")

        self.del_btn = ttk.Button(self.input_section, text="Delete")
        self.del_btn.grid(row=5, column=4, padx=0, pady=10, sticky="w")
        
        self.edit_btn = ttk.Button(self.input_section, text="edit")
        self.edit_btn.grid(row=5, column=5, padx=0, pady=10, sticky="w")

        #scrooll 

        # Preview Section
        self.preview_section = ttk.LabelFrame(self, text="Preview")
        self.preview_section.grid(row=0, column=1, padx=20, pady=10, sticky="nsew")

        # Define Columns for TreeView
        cols = ('REF_NO','EFFECTIVE_DATE','BEN_CODE','BEN_DESC','SEC_CODE','SEC_TYPE','PER_WEIGHT','USER_UPLOAD','UPLOAD_DATE','DELETE_FLAG',"ID")
        self.preview_tree = ttk.Treeview(
            self.preview_section, show="headings", columns=cols, height=20, 
            )
        for col in cols:
            self.preview_tree.heading(col, text=col)
            self.preview_tree.column(col, width=150 if col != "ID" else 0)  # Hide ID column
                
        # Add Scrollbar
        tree_scroll = ttk.Scrollbar(self.preview_section, orient="vertical", command=self.preview_tree.yview)
        tree_scroll.pack(side="right", fill="y")
        tree_scrollx = ttk.Scrollbar(self.preview_section, orient="horizontal", command=self.preview_tree.xview)
        tree_scrollx.pack(side="bottom", fill="x")

        # Configure TreeView to work with Scrollbar
        self.preview_tree.configure(xscrollcommand=tree_scrollx.set,yscrollcommand=tree_scroll.set)
#        self.preview_tree.configure(xscrollcommand=tree_scrollx.set)

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


#----------------------validate------------------

    def validate_ben_code(self, event):
            """Validate BEN_CODE input: maximum 10 characters, alphanumeric, and specific special characters."""
            input_data = self.BEN_CODE_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _]*$'
            if len(input_data) > 10:
                self.BEN_CODE_input.delete(10, tk.END)
                messagebox.showwarning("Validation Error", "BEN_CODE cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.BEN_CODE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "BEN_CODE can only contain alphanumeric characters, '/', '_', and '|'.")

    def validate_sec_code(self, event):
            """Validate BEN_CODE input: maximum 10 characters, alphanumeric, and specific special characters."""
            input_data = self.SEC_CODE_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _]*$'
            if len(input_data) > 20:
                self.SEC_CODE_input.delete(20, tk.END)
                messagebox.showwarning("Validation Error", "cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.SEC_CODE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "can only contain alphanumeric characters, '/', '_', and '|'.")

    def validate_ben_des_code(self, event):
            """Validate BEN_CODE input: maximum 10 characters, alphanumeric, and specific special characters."""
            input_data = self.BEN_DESC_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _]*$'
            if len(input_data) > 10:
                self.BEN_DESC_input.delete(10, tk.END)
                messagebox.showwarning("Validation Error", "cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.BEN_DESC_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "can only contain alphanumeric characters, '/', '_', and '|'.")

    def validate_sec_type(self, event):
            """Validate BEN_CODE input: maximum 10 characters, alphanumeric, and specific special characters."""
            input_data = self.SEC_TYPE_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _]*$'
            if len(input_data) > 10:
                self.SEC_TYPE_input.delete(10, tk.END)
                messagebox.showwarning("Validation Error", "cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.SEC_TYPE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "can only contain alphanumeric characters, '/', '_', and '|'.")

    def validate_per_weight(self, event):
            """Validate PER_WEIGHT: must be numeric with a 5,2 format."""
            input_data = self.PER_WEIGHT_input.get()
            try:
                value = float(input_data)
                integer_part, decimal_part = input_data.split(".")
                if len(integer_part) > 5 or len(decimal_part) > 2:
                    raise ValueError("PER_WEIGHT must follow the format 5,2 (e.g., 12345.67).")
            except ValueError:
                self.PER_WEIGHT_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "PER_WEIGHT must be numeric and follow the format 5,2.")

#------------------------------test---------------------------

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Benchmark View Test")
    root.geometry("1200x600")  # Adjust window size as needed
    
    # Initialize and pack the BenchmarkView
    benchmark_view = BenchmarkView(root)
    benchmark_view.pack(fill="both", expand=True)
    
    # Run the application
    root.mainloop()