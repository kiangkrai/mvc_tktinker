from tkinter import Frame, Label, Entry, Button, ttk
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import re



class Net_Expo(Frame):
    def __init__(self, parent, *args, **kwargs):
        super().__init__(parent, *args, **kwargs)
        #Filed :REF_NO	CLIENT_CODE	RULE_CODE	USER_UPLOAD	UPLOAD_DATE	DELETE_FLAG

      

        self.input_section = ttk.LabelFrame(self,text='Net Exposire Page')
        self.input_section.grid(row=0, column=0, padx=20, pady=10)


        self.export_btn = ttk.Button(self.input_section,text="Export to csv")
        self.export_btn.grid(row=0, column=2, padx=5, pady=10,sticky="w")

        self.import_btn = ttk.Button(self.input_section, text="Import CSV", style="TButton")
        self.import_btn.grid(row=0, column=1, padx=10, pady=5, sticky="w")

       
        self.ref_no_lb = ttk.Label(self.input_section, text="REF NO")
        self.ref_no_lb.grid(row=1, column=0, padx=5, pady=10)
        self.ref_no_input = ttk.Entry(self.input_section)
        self.ref_no_input.grid(row=1, column=1, padx=5, pady=10)

        self.effect_dt_lb = ttk.Label(self.input_section,text="EFFECTIVE_DATE")
        self.effect_dt_lb.grid(row=2, column=0, padx=5, pady=10)
        self.effect_dt_input = ttk.Entry(self.input_section)
        self.effect_dt_input.grid(row=2, column=1, padx=5, pady=10)

        self.EXP_CODE_lb = ttk.Label(self.input_section,text="EXP_CODE")
        self.EXP_CODE_lb.grid(row=3, column=0, padx=5, pady=10)
        self.EXP_CODE_input = ttk.Entry(self.input_section)
        self.EXP_CODE_input.grid(row=3, column=1, padx=5, pady=10)
        self.EXP_CODE_input.bind("<KeyRelease>", self.validate_EXP_CODE)

        self.CLIENT_CODE_lb = ttk.Label(self.input_section,text="CLIENT_CODE")
        self.CLIENT_CODE_lb.grid(row=4, column=0, padx=5, pady=10)
        self.CLIENT_CODE_input = ttk.Entry(self.input_section)
        self.CLIENT_CODE_input.grid(row=4, column=1, padx=5, pady=10)
        self.CLIENT_CODE_input.bind("<FocusOut>", self.validate_CLIENT_CODE)


        self.NET_EXPOSURE_lb = ttk.Label(self.input_section,text="NET_EXPOSURE")
        self.NET_EXPOSURE_lb.grid(row=5, column=0, padx=5, pady=10)
        self.NET_EXPOSURE_input = ttk.Entry(self.input_section)
        self.NET_EXPOSURE_input.grid(row=5, column=1, padx=5, pady=10)
        self.NET_EXPOSURE_input.bind("<FocusOut>", self.validate_NET_EXPOSURE)

        self.VAR_lb = ttk.Label(self.input_section,text="VAR")
        self.VAR_lb.grid(row=6, column=0, padx=5, pady=10)
        self.VAR_input = ttk.Entry(self.input_section)
        self.VAR_input.grid(row=6, column=1, padx=5, pady=10)
        self.VAR_input.bind("<FocusOut>", self.validate_VAR)

        self.DELETE_FLAG_lb = ttk.Label(self.input_section,text="DELETE_FLAG")
        self.DELETE_FLAG_lb.grid(row=7, column=0, padx=5, pady=10)
        self.DELETE_FLAG_input = ttk.Combobox(self.input_section, values=["DELETE"],state="readonly")
        self.DELETE_FLAG_input.grid(row=7, column=1, padx=5, pady=10)


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
        		

        cols = ('REF_NO','EFFECTIVE_DATE','EXP_CODE','CLIENT_CODE','NET_EXPOSURE',"VAR",'USER_UPLOAD','UPLOAD_DATE','DELETE_FLAG',"ID")
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

    def validate_EXP_CODE(self, event):
            input_data = self.EXP_CODE_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _ -]*$'
            if len(input_data) > 10:
                self.EXP_CODE_input.delete(10, tk.END)
                messagebox.showwarning("Validation Error", "EXP_CODE cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.EXP_CODE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "EXP_CODE can only contain alphanumeric characters, '/', '_', and '|'.")


    def validate_CLIENT_CODE(self, event):
            input_data = self.CLIENT_CODE_input.get()
            allowed_pattern = r'^[a-zA-Z0-9 _ -]*$'
            if len(input_data) > 10:
                self.CLIENT_CODE_input.delete(10, tk.END)
                messagebox.showwarning("Validation Error", "This filed cannot exceed 10 characters.")
            elif not re.match(allowed_pattern, input_data):
                self.CLIENT_CODE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "This filed can only contain alphanumeric characters, '/', '_', and '|'.")



    def validate_NET_EXPOSURE(self, event):
            """Validate PER_WEIGHT: must be numeric with a 5,2 format."""
            input_data = self.NET_EXPOSURE_input.get()
            try:
                value = float(input_data)
                integer_part, decimal_part = input_data.split(".")
                if len(integer_part) > 22 or len(decimal_part) > 2 :
                    raise ValueError("NET_LIAB must follow the format 22,2 (e.g., 12345.67).")
            except ValueError:
                self.NET_EXPOSURE_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "NET_LIAB must be numeric and follow the format 22,2.")

    def validate_VAR(self, event):
            """Validate PER_WEIGHT: must be numeric with a 5,2 format."""
            input_data = self.VAR_input.get()
            try:
                value = float(input_data)
                integer_part, decimal_part = input_data.split(".")
                if len(integer_part) > 22 or len(decimal_part) > 2 :
                    raise ValueError("This filed must follow the format 22,2 (e.g., 12345.67).")
            except ValueError:
                self.VAR_input.delete(0, tk.END)
                messagebox.showwarning("Validation Error", "This filed must be numeric and follow the format 22,2.")
#------------------------------test---------------------------

if __name__ == "__main__":
    # Create the main application window
    root = tk.Tk()
    root.title("Benchmark View Test")
    root.geometry("1200x600")  # Adjust window size as needed
    
    # Initialize and pack the BenchmarkView
    benchmark_view = Net_Expo(root)
    benchmark_view.pack(fill="both", expand=True)
    
    # Run the application
    root.mainloop()