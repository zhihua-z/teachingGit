import tkinter as tk

from Page import Page
from Book import Chapter, DBChapter 
import Styles

from datetime import datetime

class ContentPage(Page):
    
    def __init__(self, app):
        super().__init__(app)
        
        self.frame = None
    
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width = 150, height = 700, background = Styles.contentPageColor)
        self.frame.place(x = 0, y = 0)
        self.register(self.frame)
        
        count = 0
        for c in self.app.book.chapters:
            tname = c.title
            
            if c.status == 'Changed':
                tname = c.title + '*'
            self.newFile = tk.Button(master = self.frame
                                     , text = tname
                                     , command = lambda chapter = c: self.changeChapter(chapter)
                                     , highlightbackground = Styles.contentPageColor
                                     , foreground = Styles.selectedColor if c.id == self.app.currentChapter.id else Styles.foregroundColor
                                     )
            self.newFile.bind('<Button-2>', lambda event, chapter = c: self.show_popup(event, chapter))
            self.newFile.place(x = 5, y = 5 + count * 40)
            
            count += 1
            
    def show_popup(self, event, chapter):
        self.app.rightMenu.menu.delete(0, tk.END)  # Clear the existing menu items
        self.app.rightMenu.menu.add_command(label="Save", command=lambda c = chapter: self.deleteChapter(c))
        self.app.rightMenu.menu.add_command(label="Export", command=lambda c = chapter: self.deleteChapter(c))
        self.app.rightMenu.menu.add_command(label="Delete", command=lambda c = chapter: self.deleteChapter(c))
        self.app.rightMenu.menu.post(event.x_root, event.y_root)
    
    # lambda chapter = c:self.deleteChapter(chapter)
    def deleteChapter(self, chapter):
        print(chapter.id)
        
        
    def addChapter(self, chapter):
        self.app.book.addChapter(chapter)
        self.app.refresh()
        
    def changeChapter(self, chapter):
        self.app.currentChapter = chapter
        self.app.refresh()