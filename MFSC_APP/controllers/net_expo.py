from models.net_expo_model import Net_Expo_Model
from views.main import View


class Net_ExpoController:
    def __init__(self, model: Net_Expo_Model, view: View) -> None:
        self.model = Net_Expo_Model()
        self.view = view
        self.frame = self.view.frames["NetExpo"]
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
            "EXP_CODE": self.frame.EXP_CODE_input.get(),
            'CLIENT_CODE' : self.frame.CLIENT_CODE_input.get(),
            "NET_EXPOSURE" : self.frame.NET_EXPOSURE_input.get(),
            "VAR"          : self.frame.VAR_input.get(),
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
            "EXP_CODE": self.frame.EXP_CODE_input.get(),
            'CLIENT_CODE' : self.frame.CLIENT_CODE_input.get(),
            "NET_EXPOSURE" : self.frame.NET_EXPOSURE_input.get(),
            "VAR"          : self.frame.VAR_input.get(),
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

        self.frame.EXP_CODE_input.delete(0, "end")
        self.frame.EXP_CODE_input.insert(0, values[2])

        self.frame.CLIENT_CODE_input.delete(0, "end")
        self.frame.CLIENT_CODE_input.insert(0, values[3])

        
        self.frame.NET_EXPOSURE_input.delete(0, "end")
        self.frame.NET_EXPOSURE_input.insert(0, values[4])


        self.frame.VAR_input.delete(0, "end")
        self.frame.VAR_input.insert(0, values[5])

        self.frame.delete_input.delete(0, "end")
        self.frame.delete_input.insert(0, values[8])    
        

    def home(self) -> None:
        self.view.switch("Home Page")
    
    def import_csv(self):
        self.model.import_csv()
        self.load_data()