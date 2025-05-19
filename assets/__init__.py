def __init__():
    """ function to be called from main.py """

# function to run each __main__ function from each other file in /assets/
import importlib
import os

def run_all_main_functions():
    assets_dir = os.path.dirname(__file__)
    for filename in os.listdir(assets_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = f"assets.{filename[:-3]}"
            module = importlib.import_module(module_name)
            if hasattr(module, "__main__"):
                module.__main__()