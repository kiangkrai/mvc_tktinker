from models.clientxrule_model import ClientXRuleModel
from views.main import View


class ClientxRuleController:
    def __init__(self, model: ClientXRuleModel, view: View) -> None:
        self.model = ClientXRuleModel()
        self.view = view
        self.frame = self.view.frames["ClientxRule"]
        self._bind()

    def _bind(self) -> None:
        self.frame.home_page_btn.config(command=self.home)
        self.frame.add_btn.config(command=self.add_entry)
        self.frame.del_btn.config(command=self.delete_entry)
        self.frame.edit_btn.config(command=self.edit_entry)
        
        # Load data when initializing
        self.load_data()

    def load_data(self):
       """Load data from the model and display it in the TreeView."""
       data = self.model.load_data()
       self.frame.populate_treeview(data)

    def add_entry(self):
        """Handle adding a new entry (logic omitted for brevity)."""
        pass

    def delete_entry(self):
        """Handle deleting an entry (logic omitted for brevity)."""
        pass

    def edit_entry(self):
        """Handle editing an entry (logic omitted for brevity)."""
        pass


    def home(self) -> None:
        self.view.switch("Home Page")