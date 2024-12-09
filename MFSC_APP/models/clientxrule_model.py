import pandas as pd
import uuid
from tkinter import filedialog, Tk

class ClientXRuleModel:
    def  __init__(self):
        self.filepath = r"D:\MFSC_PROGRAM\UAT\MFSC_APP\asset\clientxrule_template.xlsx"
        self.data = None
    
    def load_data(self):
        try:
            self.data = pd.read_excel(self.filepath)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["ID", "REF_NO", "Client Code", "Rule Code", "USER_UPLOAD", "UPLOAD_DATE", "DELETE_FLAG"])
        
        # Ensure every row has a unique ID
        if "ID" not in self.data.columns:
            self.data["ID"] = [str(uuid.uuid4()) for _ in range(len(self.data))]
        return self.data
        
    def save_data(self):
        self.data.to_excel(self.filepath,index=False)
    
    def show_top(self, n=5):
        if self.data is None:
            self.load_data()
        return self.data.head(n)

    def add_entry(self, new_row):

        new_row["ID"] = str(uuid.uuid4())  # Generate a unique ID
        self.data = self.data._append(new_row, ignore_index=True)
        self.save_data()

    def get_row_by_id(self, row_id):

        return self.data[self.data["ID"] == row_id]

    def update_row_by_id(self, row_id, updated_row):

        self.data.loc[self.data["ID"] == row_id, updated_row.keys()] = updated_row
        self.save_data()

    def delete_row_by_id(self, row_id):

        self.data = self.data[self.data["ID"] != row_id]
        self.save_data()

    def export_data(self):
        if self.data is None:
            print("No data to export. Load or create data first.")
            return
        root = Tk()
        root.withdraw()  # Hide the root window
        output_filepath = filedialog.asksaveasfilename(
            title="Save CSV File",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv")],
            initialfile="clientXrule.csv",
            initialdir="D:\\"
        )
        root.destroy()

        export_columns = ["REF_NO", "CLIENT_CODE", "RULE_CODE", "USER_UPLOAD", "UPLOAD_DATE", "DELETE_FLAG"]
        try:
            export_data = self.data[export_columns]
            export_data.to_csv(output_filepath, sep='|', encoding='utf-8', index=False)
            print(f"Data exported successfully to {output_filepath}")
        except Exception as e:
            print(f"An error occurred while exporting data: {e}")



'''
def test_clientxrule_model():
    # Initialize the model
    model = ClientXRuleModel()

    # Load data (or create a new dataset)
    print("Loading data...")
    data = model.load_data()
    print("Data loaded successfully.")
    print(data)

    # Add a new entry
    print("\nAdding a new entry...")
    new_row = {
        "REF_NO": "TEST123",
        "CLIENT_CODE": "CLIENT001",
        "RULE_CODE": "RULE001",
        "USER_UPLOAD": "TEST_USER",
        "UPLOAD_DATE": "2024-12-09",
        "DELETE_FLAG": "N"
    }
    model.add_entry(new_row)
    print("Entry added successfully.")
    print(model.data)

    # Get a row by ID
    print("\nRetrieving a row by ID...")
    row_id = model.data.iloc[-1]["ID"]  # Get the ID of the last added row
    retrieved_row = model.get_row_by_id(row_id)
    print("Retrieved row:")
    print(retrieved_row)

    # Update the row by ID
    print("\nUpdating the row...")
    updated_row = {
        "REF_NO": "UPDATED123",
        "CLIENT_CODE": "UPDATED_CLIENT",
        "RULE_CODE": "UPDATED_RULE",
        "DELETE_FLAG": "Y"
    }
    model.update_row_by_id(row_id, updated_row)
    print("Row updated successfully.")
    print(model.get_row_by_id(row_id))

    # Delete the row by ID
    print("\nDeleting the row...")
    model.delete_row_by_id(row_id)
    print("Row deleted successfully.")
    print(model.data)

    # Save the data
    print("\nSaving data...")
    model.save_data()
    print("Data saved successfully.")

# Run the test
if __name__ == "__main__":
    test_clientxrule_model()

'''
