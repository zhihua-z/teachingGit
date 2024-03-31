import tkinter as tk

from Pages.ToolPage import ToolPage
from Pages.WriteArea import WriteArea
from Pages.ContentPage import ContentPage
from Pages.StatusBar import StatusBar

from Book import Book, Chapter


class App:
    
    def __init__(self):
        self.window = None
        self.fcontent = None
        self.f1 = None
        self.f2 = None
        
        self.toolPage = None
        self.writeArea = None
        self.contentPage = None
        
        self.current_filename = ''
        
        self.book = Book('新书')
        self.currentChapter = None

    def handleKeyPress(self, event):
            self.statusBar.draw()

    def handleKeyAutoSave(self, event):
        if event.state == 4 and event.keysym.lower() == "s":
            self.toolPage.save_file()
            self.currentChapter.status = 'Ok'
            self.currentChapter.prevContent = self.currentChapter.content
            self.refresh()
    
    def draw(self):
        # 只是创建了一个window
        self.window = tk.Tk()
        self.window.geometry("1250x725")
        
        self.window.bind("<Key>", self.handleKeyPress)
        self.window.bind("<Control-s>", self.handleKeyAutoSave)
        self.window.bind("<KeyRelease>", self.inputChanged)

        self.contentPage = ContentPage(self)
        self.writeArea = WriteArea(self)
        self.toolPage = ToolPage(self)
        self.statusBar = StatusBar(self)
        
        self.contentPage.draw()
        self.writeArea.draw()
        self.toolPage.draw()
        self.statusBar.draw()
        
    def refresh(self):
        self.contentPage.draw()
        self.writeArea.draw()
        self.toolPage.draw()
        self.statusBar.draw()
        
    
    def getPage(self, pageName):
        if pageName == 'WriteArea':
            return self.writeArea
        
        if pageName == 'ContentPage':
            return self.contentPage
        
        if pageName == 'ToolPage':
            return self.toolPage
        
        return None
    
    def inputChanged(self, event):
        self.writeArea.changed()
        
        if self.currentChapter.prevContent.rstrip() != self.currentChapter.content.rstrip() and self.currentChapter.status == 'Ok':
            self.currentChapter.status = 'Changed'
        self.contentPage.draw()
        
        self.currentChapter.prevContent = self.currentChapter.content

    def run(self):
        # 这个mainloop会不停的监听任何事件的发生，然后重画这个window
        self.window.mainloop()