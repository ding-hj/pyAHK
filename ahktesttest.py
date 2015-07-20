import pywinauto
import time

pwa_app = pywinauto.application.Application()
pwa_app.start_('notepad.exe')
 
#Type some keys into the editbox
pwa_app.UntitledNotepad.Edit.TypeKeys("test{SPACE}from{SPACE}pywinauto")
 
#Get handle to the window
w_handle = pywinauto.findwindows.find_windows(title=u'Untitled - Notepad', class_name='Notepad')[0]
window = pwa_app.window_(handle=w_handle)

time.sleep(5) # delays for 5 seconds
#Get text from the edit box
edit = window['Edit']
props = edit.GetProperties()
print props['Texts']

time.sleep(5) # delays for 5 seconds
#Trigger the About menu item
window.MenuItem(u'&Help->&About Notepad').Click()