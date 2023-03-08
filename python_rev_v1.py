import sys
import subprocess
import os

def install(module_name):
    """
    Install the module corresponding to the name provided.
    :param module_name: String, Name of the module to be installed.
    """
    subprocess.call(['pip', 'install', '--trusted-host', 'pypi.org', '--trusted-host', 'files.pythonhosted.org', module_name])

try:
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import ttk
except:
    install("tk")
    import tkinter as tk
    from tkinter import filedialog
    from tkinter import ttk
    

def select_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    return file_path

path = select_file()