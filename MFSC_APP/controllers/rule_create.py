from models.main import Model
from views.main import View


class RuleController:
    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view
        self.frame = self.view.frames["Rule Create"]
        self._bind()

    def _bind(self) -> None:
        self.frame.home_page_btn.config(command=self.home)
        self.frame.append_profiles_btn.config(command=self.load_data)

    def home(self) -> None:
        self.view.switch("Home Page")
    
    def load_data(self)-> None:
        data = self.model.rule.load_data()
        self.frame.populate_treeview(data)
