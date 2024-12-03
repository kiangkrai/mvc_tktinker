from models.main import Model
from views.main import View

class HomeController:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        self.frame = self.view.frames["Home Page"]
        self._bind()

    def _bind(self):
        self.frame.rule_page_btn.config(command=self.rule_create)
    
    def rule_create(self) -> None:
        self.view.switch("Rule Create")
