from models.main import Model
from views.main import View
from controllers.main import Controller
from models.clientxrule_model import ClientXRuleModel

def main():
    view = View()
    controller = Controller(view)
    controller.start()

if __name__ == "__main__":
    main()