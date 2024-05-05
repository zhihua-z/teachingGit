import tkinter as tk

from Pages.ToolPage import ToolPage
from Pages.WriteArea import WriteArea
from Pages.ContentPage import ContentPage
from Pages.StatusBar import StatusBar
from Pages.LoginPage import LoginPage
from Pages.WelcomePage import WelcomePage
from Pages.RIghtMenu import RightMenu
from Book import Book, Chapter, DBBook, DBChapter 
from DBconnection import DBconnection

class App:
    
    def __init__(self):
        self.window = None
        self.fcontent = None
        self.f1 = None
        self.f2 = None

        self.db = DBconnection('mydb.db')
        
        self.toolPage = None
        self.writeArea = None
        self.contentPage = None
        self.statusBar = None
        self.loginPage = None
        self.welcomePage = None
        
        self.current_filename = ''
        
        self.book = None
        self.currentBookId = 0 # because 0 is illegal ID in database, so it's kind of the same as None
        self.currentChapterId = 0
        self.currentBook = None
        self.currentChapter = None
        
        self.userid = None
        self.username = None
        
        # array of books retrieved from database
        self.userbook = None
        self.recentbook = None

        self.loggedin = False
        self.openedBook = False
        

        self.contentPage = ContentPage(self)
        self.writeArea = WriteArea(self)
        self.toolPage = ToolPage(self)
        self.statusBar = StatusBar(self)
        self.loginPage = LoginPage(self)
        self.welcomePage = WelcomePage(self)
        self.rightMenu = RightMenu(self)
        

    def handleKeyPress(self, event):
        if self.loggedin == False:
            return
        self.statusBar.draw()

    def handleKeyAutoSave(self, event):
        if event.state == 4 and event.keysym.lower() == "s":
            self.toolPage.save_file()
            self.currentChapter.status = 'Ok'
            self.currentChapter.prevContent = self.currentChapter.content
        self.refresh()
    
    def draw(self):
        if self.window is not None:
            self.window.destroy()

        self.window = tk.Tk()
        self.window.geometry("1250x725")

        if self.username is not None:
            self.window.title('Editor: ' + self.username)
        else:
            self.window.title('Online Text Editor')
        
        self.window.bind("<Key>", self.handleKeyPress)
        self.window.bind("<Control-s>", self.handleKeyAutoSave)
        self.window.bind("<KeyRelease>", self.inputChanged)
        
        self.drawMainPage()

        
    def drawMainPage(self):
        self.rightMenu.draw()
        
        if self.loggedin:
            if self.openedBook:
                self.contentPage.draw()
                self.writeArea.draw()
                self.toolPage.draw()
                self.statusBar.draw()
            else:
                self.userbook = self.retrieveUserBooks()
                self.recentbook = self.retrieveRecentBooks() 
                self.welcomePage.draw()      
        else:
            self.loginPage.draw()   
    
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
        if self.writeArea.content is None:
            return
        
        self.writeArea.changed()
        
        if self.currentChapter.prevContent.rstrip() != self.currentChapter.content.rstrip() and self.currentChapter.status == 'Ok':
            self.currentChapter.status = 'Changed'
        self.contentPage.draw()
        
        self.currentChapter.prevContent = self.currentChapter.content

    def retrieveUserBooks(self): 
        if self.loggedin == False:
            return 

        return self.db.retrieveUserBooksByUsername(self.username)

    # function delegate
    def retrieveRecentBooks(self, limit = 5):
        return self.db.retrieveRecentBooks(limit)

    def run(self):
        # 这个mainloop会不停的监听任何事件的发生，然后重画这个window
        self.window.mainloop()