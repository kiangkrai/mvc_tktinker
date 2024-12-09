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
    
    def rule_create(self) -> None:
        print("Switching to Rule Create")
        self.view.switch("Rule Create")

    
    def clientxrule_create(self) -> None:
        print("Switching to Client X Rule")
        self.view.switch("ClientxRule")
