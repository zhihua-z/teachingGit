import tkinter as tk
from datetime import datetime

from Page import Page
from Book import DBBook, DBChapter
from UI.ImageButton import Button, Label

import Styles

class WelcomePage(Page):
    
    def __init__(self, app):

        super().__init__(app)
        
        self.frame = None

        self.welcomeFont = ('Sans-Serif' , 50 , 'bold')
        self.textFont = ('Times New Roman', 18)
        
    def draw(self): 
        self.clear()
        
        self.frame = tk.Frame(width = 1250, 
                              height = 750, 
                              background=Styles.backgroundColor)
        self.frame.place(x = 0, y = 0)
        self.register(self.frame)

        self.welcome = Label(
            master = self.frame, 
            text = "Welcome, " + self.app.username, 
            font = self.welcomeFont, 
            position = ((225, 100))
        )
        self.register(self.welcome)

        t = tk.Label(master = self.frame,
                      text = "Start...",
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 200)
        self.register(t)

        t = Label(
            master = self.frame, 
            text = "Start...", 
            font = self.textFont, 
            position = ((250, 200))
        )
        self.register(t)

        t = tk.Button(master = self.frame,
                      text = "Open Book",
                      command = self.open_book,
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 250)
        self.register(t)
        
        t = tk.Button(master = self.frame,
                      text = "Create Book",
                      command = self.create_book,
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 300)
        self.register(t)

        t = Label(
            master = self.frame, 
            text = "Recent...", 
            font = self.textFont, 
            position = ((250, 400))
        )
        self.register(t)
        
        self.displayRecentBooks()

    def displayRecentBooks(self):
        recentBooks = self.app.recentbook

        if recentBooks:
            for i in range(len(recentBooks)):
                bookName = Button(master = self.frame,
                                  text = recentBooks[i][0],
                                  position=(250, 450 + i * 50),
                                  command=lambda b=recentBooks[i]: self.open_book(b))
        else:
            noResult = Label(master = self.frame,
                             text = "No Recent Books Created",
                             font = None, 
                             position=(250, 450))

    def open_book(self, book):
        
        # 1.1 get the ID of the book we created just now
        bookresult = self.app.db.retrieveBookInfoByBookId(book[2])
        self.app.currentBookId = bookresult[0][0]
        
        self.app.book = DBBook(bookresult[0][0], 
                               bookresult[0][1], 
                               bookresult[0][2], 
                               bookresult[0][3])
        
        # 1.1 get the ID of the chapter we created just now
        chapterresults = self.app.db.retrieveChaptersByBookId(bookresult[0][0])
        
        # 3. fill the book with the chapters we retrieved, set current chapter to last chapter
        for chapterresult in chapterresults:
            
            chapter = DBChapter(chapterresult[0], 
                                chapterresult[1], 
                                chapterresult[2], 
                                chapterresult[3],
                                chapterresult[4])
            self.app.book.chapters.append(chapter)
        
        
        self.app.currentChapterId = chapterresults[-1][0]
        self.app.currentChapter = self.app.book.chapters[-1]
        
        self.app.openedBook = True
        self.clear()
        self.app.draw()

    def create_book(self):
        current_time = datetime.now()
        # 1. create a new book record in the database
        self.app.db.createBook('新书', self.app.userid, current_time)
        
        # 1.1 get the ID of the book we created just now
        bookresult = self.app.db.retrieveBookByCreatedTime(current_time)
        self.app.currentBookId = bookresult[0][0]
        
        # 2. create a new chapter record in the database and link it to the new book
        self.app.db.createChapter('第1章', '', self.app.currentBookId, current_time)
        
        # 1.1 get the ID of the chapter we created just now
        chapterresult = self.app.db.retrieveChapterByCreatedTime(current_time)
        
        # 3. set current chapter to this new chapter, current book to this new book
        self.app.book = DBBook(bookresult[0][0], 
                               bookresult[0][1], 
                               bookresult[0][2], 
                               bookresult[0][3])
        
        chapter = DBChapter(chapterresult[0][0], 
                            chapterresult[0][1], 
                            chapterresult[0][2], 
                            chapterresult[0][3],
                            chapterresult[0][4])
        self.app.book.chapters.append(chapter)
        
        
        self.app.currentChapterId = chapterresult[0][0]
        self.app.currentChapter = self.app.book.chapters[0]
        
        self.app.openedBook = True
        self.clear()
        self.app.draw()