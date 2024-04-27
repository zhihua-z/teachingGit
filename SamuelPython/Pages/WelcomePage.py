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
        
    def draw(self): 
        self.clear()
        
        self.frame = tk.Frame(width = 1250, 
                              height = 750, 
                              background=Styles.backgroundColor)
        self.frame.place(x = 0, y = 0)
        self.register(self.frame)

        self.welcome = tk.Label(master = self.frame,
                               text = "Welcome, " + self.app.username,
                               font = self.welcomeFont, 
                               highlightbackground=Styles.backgroundColor, 
                               )
        self.welcome.place(x = 225, y = 100)

        t = tk.Label(master = self.frame,
                      text = "Start...",
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 200)

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

        t = tk.Label(master = self.frame,
                      text = "Recent",
                      highlightbackground = Styles.backgroundColor)
        t.place(x = 250, y = 400)
        
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
                             position=(250, 450))

    def open_book(self):
        pass
            
    def create_book(self):
        current_time = datetime.now()
        # 1. create a new book record in the database
        querystr = '''
        insert into book (name, userid, created_time)
        values (?, ?, ?)
        '''
        self.app.cursor.execute(querystr, ('新书', self.app.userid, current_time))
        
        result = self.app.cursor.fetchall()
        
        # 1.1 get the ID of the book we created just now
        querystr = '''
        select id, name, userid, created_time from book
        where created_time = ?
        '''
        self.app.cursor.execute(querystr, (current_time,))
        
        bookresult = self.app.cursor.fetchall()
        self.app.currentBookId = bookresult[0][0]
        
        
        # 2. create a new chapter record in the database and link it to the new book
        querystr = '''
        insert into chapter (title, content, bookid, created_time)
        values (?, ?, ?, ?)
        '''
        self.app.cursor.execute(querystr, ('新章节', '', self.app.currentBookId, current_time))
        
        
        # 1.1 get the ID of the chapter we created just now
        querystr = '''
        select id, title, content, bookid, created_time from chapter
        where created_time = ?
        '''
        self.app.cursor.execute(querystr, (current_time,))
        
        chapterresult = self.app.cursor.fetchall()
        
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
        
        self.app.connection.commit()
        
        
        self.app.currentChapterId = chapterresult[0][0]
        self.app.currentChapter = self.app.book.chapters[0]
        
        self.app.openedBook = True
        self.app.draw()
        
    
    def open_book(self, book):
        
        # 1.1 get the ID of the book we created just now
        querystr = '''
        select id, name, userid, created_time from book
        where id = ?
        '''
        self.app.cursor.execute(querystr, (book[2],))
        
        bookresult = self.app.cursor.fetchall()
        self.app.currentBookId = bookresult[0][0]
        
        self.app.book = DBBook(bookresult[0][0], 
                               bookresult[0][1], 
                               bookresult[0][2], 
                               bookresult[0][3])
        
        
        # 1.1 get the ID of the chapter we created just now
        querystr = '''
        select id, title, content, bookid, created_time from chapter
        where bookid = ?
        '''
        self.app.cursor.execute(querystr, (bookresult[0][0],))
        
        chapterresults = self.app.cursor.fetchall()
        
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
        self.app.draw()