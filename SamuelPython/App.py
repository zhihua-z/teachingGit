import tkinter as tk

from Pages.ToolPage import ToolPage
from Pages.WriteArea import WriteArea
from Pages.ContentPage import ContentPage

class App:
    
    def __init__(self):
        self.window = None
        self.fcontent = None
        self.f1 = None
        self.f2 = None
        
        self.toolPage = None
        self.writeArea = None
        self.ContentPage = None
        
        self.current_filename = ''
    
    def draw(self):
        # 只是创建了一个window
        self.window = tk.Tk()
        self.window.geometry("1150x700")

        self.contentPage = ContentPage(self)
        self.writeArea = WriteArea(self)
        self.toolPage = ToolPage(self)
        
        self.contentPage.draw()
        self.writeArea.draw()
        self.toolPage.draw()
        

    def run(self):
        # 这个mainloop会不停的监听任何事件的发生，然后重画这个window
        self.window.mainloop()
