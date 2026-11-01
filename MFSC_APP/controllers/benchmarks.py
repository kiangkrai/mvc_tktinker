from models.main import Model
from views.main import View
from models.benchmark_model import BenchmarkModel

class BenchmarkController:
    def __init__(self,model : BenchmarkModel ,view: View) -> None:
        self.model = BenchmarkModel()
        self.view = view
        self.frame = self.view.frames["Benchmark"]
        self._bind()

    def _bind(self) -> None:
        self.frame.home_page_btn.config(command=self.home)
        #self.frame.append_profiles_btn.config(command=self.load_data)

        #self.load_data()
        
    def home(self) -> None:
        self.view.switch("Home Page")
    '''
    def load_data(self):
       """Load data from the model and display it in the TreeView."""
       data = self.model.load_data()
       self.frame.populate_treeview(data)
    '''