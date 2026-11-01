from ttkbootstrap import Style
from ttkbootstrap.constants import *

def apply_styles():

    style = Style() # Pass the root window to ttkbootstrap's Style
    style.theme_use("cosmo")  # Choose a theme (e.g., "flatly", "darkly")
    
    # Configure styles
    style.configure("TLabel", font=("Segoe UI", 12), padding=10)
    style.configure("TButton", font=("Segoe UI", 12, "bold"), padding=10)
    style.configure("TFrame", background="#f4f4f4")  # Example frame background
    style.configure("Treeview", font=("Segoe UI", 10), rowheight=25)