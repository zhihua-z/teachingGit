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

        t = tk.Label(master = self.frame,
                      text = "Start...",
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 200)

        t = Label(
            master = self.frame, 
            text = "Start...", 
            font = self.textFont, 
            position = ((250, 200))
        )

        t = tk.Button(master = self.frame,
                      text = "Open Book",
                      command = self.open_book,
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 250)
        
        t = tk.Button(master = self.frame,
                      text = "Create Book",
                      command = self.create_book,
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 300)

        t = Label(
            master = self.frame, 
            text = "Recent...", 
            font = self.textFont, 
            position = ((250, 400))
        )
        
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
        self.app.currentBook = self.app.book
        self.app.currentBookId = bookresult[0][0]
        
        self.app.openedBook = True
        self.app.draw()

    def create_book(self):
        current_time = datetime.now()
        
        # 3. set current chapter to this new chapter, current book to this new book
        self.app.book = DBBook(id = 0, 
                               name = '新书', 
                               userid = self.app.userid, 
                               created_time = current_time,
                               localOnly = True)
        
        chapter = DBChapter(id = 0, 
                            title = '第一章', 
                            content = '', 
                            bookid = 0,
                            created_time = current_time,
                            localOnly = True)
        self.app.book.chapters.append(chapter)
        
        
        self.app.currentChapterId = 0
        self.app.currentChapter = self.app.book.chapters[0]
        self.app.currentBook = self.app.book
        self.app.currentBookId = 0
        
        self.app.openedBook = True
        self.app.draw()