import tkinter as tk

from Page import Page
from Book import Chapter

class ContentPage(Page):
    
    def __init__(self, app):
        super().__init__(app)
        
        self.frame = None
    
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width=150, height=700, background='#dddddd')
        self.frame.place(x=0, y=0)
        self.register(self.frame)
        
        count = 0
        for c in self.app.book.chapters:
            tname = c.name
            
            if c.status == 'Changed':
                tname = c.name + '*'
            self.newFile = tk.Button(master=self.frame, text=tname, command= lambda chapter = c: self.changeChapter(chapter))
            self.newFile.place(x=5, y=5 + count * 40)
            
            count += 1
        
    def addChapter(self, chapterName = '', content = '', filePath = ''):
        c = Chapter(chapterName, content, filePath)
        self.app.book.addChapter(c)
        
        self.app.refresh()
        
    def changeChapter(self, chapter):
        self.app.currentChapter = chapter
        self.app.refresh()