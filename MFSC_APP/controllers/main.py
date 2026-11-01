
from views.main import View

from .home import HomeController
from .rule_create import RuleController
from .clientxrule import ClientxRuleController
from models.clientxrule_model import ClientXRuleModel
from models.rule_model import RuleCreateModel
from models.benchmark_model import BenchmarkModel
from .benchmarks import BenchmarkController
from models.financial_liab_model import Financial_liabModel
from .financial_liab import Financial_liabController 
from models.net_expo_model import Net_Expo_Model
from .net_expo import Net_ExpoController

class Controller:
    def __init__(self, view: View):
        self.view = view
        
        # Dictionary to hold models and controllers
        self.rule_model = RuleCreateModel
        self.clientxrule_model = ClientXRuleModel
        self.rule_controller = RuleController(self.rule_model,view)
        self.home_controller = HomeController(view)
        self.clientxrule_controller = ClientxRuleController(self.clientxrule_model,view)
        self.benchmark_model = BenchmarkModel
        self.benchmark_controller = BenchmarkController(self.benchmark_model,view)
        self.financial_liab_model = Financial_liabModel
        self.financial_liab_controller = Financial_liabController(self.financial_liab_model,view)
        self.Net_Expo_Model = Net_Expo_Model
        self.Net_Expo_controller = Net_ExpoController(self.Net_Expo_Model,view)

        

        # Initialize models and controllers
       

#    def _initialize_modules(self):
 #       """Initialize models and controllers for each dataset."""
        # ClientXRule Module
  #      self.models["clientxrule"] = ClientXRuleModel()
  #           self.controllers["clientxrule"] = ClientxRuleController(self.models["clientxrule"], self.view)

        # RuleCreate Module
        #self.models["rulecreate"] = RuleCreateModel()
        #self.controllers["rulecreate"] = RuleController(self.models["rulecreate"], self.view)

    def start(self):
        """Start the application by showing the initial view."""
        # Load initial data for a default controller, e.g., home page or specific dataset
        self.view.switch("Home Page")
        self.view.start_mainloop()

''''class Controller:
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
------
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