from models.financial_liab_model import Financial_liabModel
from views.main import View


class Financial_liabController:
    def __init__(self, model: Financial_liabModel, view: View) -> None:
        self.model = Financial_liabModel()
        self.view = view
        self.frame = self.view.frames["Financial_liab"]
        self._bind()

    def _bind(self) -> None:
        self.frame.home_page_btn.config(command=self.home)
        self.frame.add_btn.config(command=self.add_entry)
        self.frame.del_btn.config(command=self.delete_entry)
        self.frame.edit_btn.config(command=self.edit_entry)
        self.frame.export_btn.config(command=self.export_csv)
        self.frame.preview_tree.bind("<<TreeviewSelect>>", self.populate_entry_boxes)
        self.frame.import_btn.config(command=self.import_csv)
        # Load data when initializing
        self.load_data()

    def load_data(self):
       """Load data from the model and display it in the TreeView."""
       data = self.model.load_data()
       self.frame.populate_treeview(data)

    def add_entry(self):
        new_row = {
            "REF_NO": self.frame.ref_no_input.get(),
            "EFFECTIVE_DATE": self.frame.effect_dt_input.get(),
            "COMP_CODE": self.frame.COMP_CODE_input.get(),
            'NET_LIAB' : self.frame.NET_LIAB_input.get(),
            "USER_UPLOAD": " ",  # Default value
            "UPLOAD_DATE": " ",
            "DELETE_FLAG": self.frame.DELETE_FLAG_input.get()
        }
        # Add new row to the model
        self.model.add_entry(new_row)
        self.load_data()

    def delete_entry(self):
        # Get the selected row's ID
        selected_item = self.frame.preview_tree.selection()
        if not selected_item:
            print("No row selected!")
            return

        row_id = self.frame.preview_tree.item(selected_item[0], "values")[0]

        # Delete the row in the model
        self.model.delete_row_by_id(row_id)
        self.load_data()

    
    def export_csv(self):
        self.model.export_data()
        
    def edit_entry(self):
        selected_item = self.frame.preview_tree.selection()
        if not selected_item:
            print("No row selected!")
            return

        row_id = self.frame.preview_tree.item(selected_item[0], "values")[0]

                # Update the row in the model
        updated_row = {
            "REF_NO": self.frame.ref_no_input.get(),
            "EFFECTIVE_DATE": self.frame.effect_dt_input.get(),
            "COMP_CODE": self.frame.COMP_CODE_input.get(),
            'NET_LIAB' : self.frame.NET_LIAB_input.get(),
            "DELETE_FLAG": self.frame.DELETE_FLAG_input.get()
        }
        self.model.update_row_by_id(row_id, updated_row)
        self.load_data()
    
    def populate_entry_boxes(self, event):
        selected_item = self.frame.preview_tree.selection()
        if not selected_item:
            return
            
        # Populate entry boxes with selected row's data
        values = self.frame.preview_tree.item(selected_item[0], "values")
        self.frame.ref_no_input.delete(0, "end")
        self.frame.ref_no_input.insert(0, values[0])

        self.frame.effect_dt_input.delete(0, "end")
        self.frame.effect_dt_input.insert(0, values[1])

        self.frame.COMP_CODE_input.delete(0, "end")
        self.frame.COMP_CODE_input.insert(0, values[2])

        self.frame.NET_LIAB_input.delete(0, "end")
        self.frame.NET_LIAB_input.insert(0, values[3])

        self.frame.delete_input.delete(0, "end")
        self.frame.delete_input.insert(0, values[6])    


    def home(self) -> None:
        self.view.switch("Home Page")
    
    def import_csv(self):
        self.model.import_csv()
        self.load_data()