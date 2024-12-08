from models.main import Model
from views.main import View

from .home import HomeController
from .rule_create import RuleController
from .clientxrule import ClientxRuleController

class Controller:
    def __init__(self, model: Model, view: View) -> None:
        self.view = view
        self.model = model
        self.rule_controller = RuleController(model, view)
        self.home_controller = HomeController(model, view)
        self.clientxrule_controller = ClientxRuleController(model, view)

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        self.rule_controller.load_data()
        self.view.switch("Home Page")
        self.view.start_mainloop()        




'''
    def auth_state_listener(self, data: Auth) -> None:
        if data.is_logged_in:
            self.home_controller.update_view()
            self.view.switch("home")
        else:
            self.view.switch("signin")

    def start(self) -> None:
        # Here, you can do operations required before launching the gui, for example,
        # self.model.auth.load_auth_state()
        if self.model.auth.is_logged_in:
            self.view.switch("home")
        else:
            self.view.switch("signin")

        self.view.start_mainloop()'''