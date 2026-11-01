from models.main import Model
from views.main import View

class HomeController:
    def __init__(self, view):
        self.view = view
        self.frame = self.view.frames["Home Page"]
        self._bind()

    def _bind(self):
        self.frame.rule_page_btn.config(command=self.rule_create)
        self.frame.clientxrule_page_btn.config(command=self.clientxrule_create)
        self.frame.benmark_page_btn.config(command=self.benchmark)
        self.frame.finacial_liab_page_btn.config(command=self.finacial_liab)
        
        self.frame.Net_Expo_page_btn.config(command=self.Net_Expo)
        
    
    def rule_create(self) -> None:
        print("Switching to Rule Create")
        self.view.switch("Rule Create")

    
    def Net_Expo(self) -> None:
        print("Switching to Exposure")
        self.view.switch("NetExpo")


    def finacial_liab(self) -> None:
        print("Switching to finacial_liab")
        self.view.switch("Financial_liab")

    def benchmark(self) -> None:
        print("Switching to Benchmark")
        self.view.switch("Benchmark")
    
    def clientxrule_create(self) -> None:
        print("Switching to Client X Rule")
        self.view.switch("ClientxRule")
