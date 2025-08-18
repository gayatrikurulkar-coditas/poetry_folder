import runpy
import sys

def run():
    if len(sys.argv) < 2:
        print("Usage: poetry run main <module_name>")
        sys.exit(1)
    mod_name = sys.argv[1]
    runpy.run_module(mod_name, run_name="main")
