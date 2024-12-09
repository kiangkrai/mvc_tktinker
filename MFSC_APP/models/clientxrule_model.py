import pandas as pd


class ClientXRuleModel:
    def  __init__(self):
        self.filepath = r"D:\MFSC_PROGRAM\UAT\MFSC_APP\asset\clientxrule_template.xlsx"
        self.data = None
    
    def load_data(self):
        try:
            self.data = pd.read_excel(self.filepath)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=["REF_NO", "Client Code", "Rule Code", "USER_UPLOAD", "UPLOAD_DATE", "DELETE_FLAG"])
            #self.save_data()
        return self.data
        
    def save_data(self):
        self.data.to_excel(self.filepath,index=False)
    
    def show_top(self, n=5):
        if self.data is None:
            self.load_data()
        return self.data.head(n)
    

'''''
# Testing Function
def main():
    # Create an instance of ClientXRuleModel
    model = ClientXRuleModel()
    
    # Load the data
    print("Loading data...")
    data = model.load_data()
    print("Data loaded successfully.")
    
    # Show top rows
    print("Top rows of the dataset:")
    print(model.show_top())

    # Test save functionality (optional)
    print("Testing save functionality...")
    model.save_data()
    print("Data saved successfully.")

if __name__ == "__main__":
    main()

'''
    

