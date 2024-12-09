from models.main import Model
from views.main import View
from models.rule_model import RuleCreateModel

class RuleController:
    def __init__(self,model : RuleCreateModel ,view: View) -> None:
        self.model = RuleCreateModel()
        self.view = view
        self.frame = self.view.frames["Rule Create"]
        self._bind()

    def _bind(self) -> None:
        self.frame.home_page_btn.config(command=self.home)
        self.frame.append_profiles_btn.config(command=self.load_data)

        self.load_data()
        
    def home(self) -> None:
        self.view.switch("Home Page")
    
    def load_data(self):
       """Load data from the model and display it in the TreeView."""
       data = self.model.load_data()
       self.frame.populate_treeview(data)