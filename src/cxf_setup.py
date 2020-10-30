import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

exe=Executable(
     script="main.py",
     base=base,
     icon="../img/rushHour.icns"
     )

includefiles=["../img/rushHour.icns"]
includes=[]
excludes=[]
packages=["os", "sys", "tkinter",'model','controller','view','view.levels']

setup(

     version = "1.0",
     description = "Rush Hour Game",
     author = "Michotte Martin",
     name = "RushHour",
     options = {'build_exe': {'includes':includes,'excludes':excludes,'packages':packages,'include_files':includefiles}},
     executables = [exe]
)