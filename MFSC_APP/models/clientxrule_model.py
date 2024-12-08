import pandas as pd
from config.templates import TEMPLATE_PATHS


class ClientXRuleModel:
    def  __init__(self, filepath):
        self.filepath = TEMPLATE_PATHS['ClientXRule']
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
    