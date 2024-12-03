import pandas as pd

class RuleCreateModel:
    def  __init__(self, filepath):
        self.filepath = filepath 
        self.data = None
    
    def load_data(self):
        try:
            self.data = pd.read_excel(self.filepath)
        except FileNotFoundError:
            self.data = pd.DataFrame(columns=['REF_NO', 'RULE_CODE', 'RULE_DESCRIPTION', 'FORMULA', 'OPEN_PARENTHESIS',
                    'CONDITION', 'OPERATOR1', 'CONDITION_VALUE', 'AND_OR1', 'CLOSE_PARENTHESIS',
                    'AND_OR2', 'OPERATOR2', 'LIMIT_VALUE', 'BENCHMARK_CODE', 'PRORATA', 'CIS_MANAGER',
                    'MKT_DERIVATIVE', 'UNDERLYING_CODE', 'REMARK', 'DELETE_FLAG', 'USER_UPLOAD', 'UPLOAD_DATE'])
            self.save_data()
        return self.data
        
    def save_data(self):
        self.data.to_excel(self.filepath,index=False)
    
    def show_top(self, n=5):
        if self.data is None:
            self.load_data()
        return self.data.head(n)
    
    


'''test_file = r'D:\MFSC_PROGRAM\MFSC_APP\asset\rule_code_temp.xlsx'

rulemodel = RuleCreateModel(test_file)

data = rulemodel.show_top(2)
print(data)
'''

