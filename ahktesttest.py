__author__ = 'XelnectPC'
from pywinauto.application import Application
app = Application.start("notepad.exe")
app.Notepad.Edit
app.Notepad.Edit.TypeKeys("Hello World ")
#Type some keys into the editbox
app.UntitledNotepad.Edit.TypeKeys("test{SPACE}from{SPACE}pywinauto")
