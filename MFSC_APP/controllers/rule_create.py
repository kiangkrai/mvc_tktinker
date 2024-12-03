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

    def home(self) -> None:
        self.view.switch("Home Page")
