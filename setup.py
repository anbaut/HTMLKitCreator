from cx_Freeze import setup, Executable
import os

os.environ['TCL_LIBRARY'] = r'C:\Users\tpenhard\AppData\Local\Programs\Python\Python36-32\tcl\tcl8.6'
os.environ['TK_LIBRARY'] = r'C:\Users\tpenhard\AppData\Local\Programs\Python\Python36-32\tcl\tk8.6'


setup(
        name = "HTMLKitCreator",
        version = "1.0",
        description = "créateur de kits html",
        executables = [Executable("HTMLKitCreator.py")])