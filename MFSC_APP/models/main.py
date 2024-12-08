from .rule_model import RuleCreateModel

class Model:
    def __init__(self):
        test_file = r'D:\MFSC_PROGRAM\MFSC_APP\asset\rule_code_temp.xlsx'
        self.rule = RuleCreateModel(test_file)
