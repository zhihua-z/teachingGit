import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfilename

from Page import Page
from Book import DBBook, DBChapter

from UI.ImageButton import ImageButton, Label

import Styles

from datetime import datetime

class ToolPage(Page):
    
    def __init__(self, app):
        super().__init__(app)
        self.open_file_button = None
        self.app = app
    
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(background = Styles.backgroundColor, 
                              width = 400, 
                              height = 700)
        self.frame.place(x = 950, y = 0)
        self.register(self.frame)
        
        t = ImageButton(
            master = self.frame, 
            filename = 'img/open_file.png', 
            size = (25, 25), 
            position = (10, 10), 
            command = self.import_text_file,
            text = 'Import file'
        )
        self.registerUI(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'img/save_file.png',
            size = (25, 25),
            position = (110, 10),
            command = self.export_text_file,
            text = 'Export file'
        )
        self.registerUI(t)
        
        t = ImageButton(
            master = self.frame, 
            filename = 'img/new_file.png',
            size = (25, 25),
            position = (210, 10),
            command = self.new_file,
            text = 'New file'
        )
        self.registerUI(t)

        t = Label(
            master = self.frame,
            text = 'Font',
            font = None, 
            position = ((10, 100)),
        )
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = 'Font type',
            highlightbackground = Styles.backgroundColor
        )
        t.place(x = 10, y = 135)
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = 'Font size',
            highlightbackground = Styles.backgroundColor
        )
        t.place(x = 110, y = 135)
        self.register(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'img/bold.png',
            size = (25, 25),
            position = (10, 185),
            command = self.app.writeArea.setBold,
            text = 'Bold text'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'img/italic.png',
            size = (25, 25),
            position = (95, 185),
            command = self.app.writeArea.setItalic,
            text = 'Italic text'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'img/underline.png',
            size = (25, 25),
            position = (180, 185),
            command = None,
            text = 'Underline text'
        )
        self.registerUI(t) 

        t = tk.Button(
            master = self.frame,
            text = 'Text color', 
            highlightbackground = Styles.backgroundColor, 
        )
        t.place(x = 10, y = 260)
        self.register(t)

        t = tk.Button(
            master = self.frame,
            text = "Highlight color",
            highlightbackground = Styles.backgroundColor,
        )
        t.place(x = 110, y = 260)
        self.register(t)

        t = Label(
            master = self.frame,
            text = 'Align',
            font = None, 
            position = ((10, 315))
        )
        self.register(t)

        t = ImageButton(
            master = self.frame, 
            filename = 'img/align_left.png',
            size = (25, 25),
            position = (10, 360),
            command = None,
            text = 'Align text to left'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'img/align_right.png',
            size = (25, 25),
            position = (160, 360),
            command = None,
            text = 'Align text to right'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'img/align_center.png',
            size = (25, 25),
            position = (10, 440),
            command = None,
            text = 'Align text to center'
        )
        self.registerUI(t) 

        t = ImageButton(
            master = self.frame, 
            filename = 'img/justify.png',
            size = (25, 25),
            position = (160, 440),
            command = None, 
            text = 'Justify text'
        )
        self.registerUI(t) 

    def open_file(self):
        self.import_text_file(self)

    def import_text_file(self):
        self.app.current_filename = askopenfilename()
        f = open(self.app.current_filename, "r")
        text = f.read()

        if self.app.current_filename:

            self.app.contentPage.addChapter(content = text, filePath = self.app.current_filename)
            # To get the last page as the current page 
            self.app.currentChapter = self.app.book.chapters[-1]
            self.app.writeArea.draw()
            self.app.refresh()

    def save_file(self):
        # save the current chapter to db
        # change the state to saved

        current_time = datetime.now()
        
        book = self.app.currentBook
        if book is not None and book.localOnly:
            
            # 1. create a new book record in the database
            self.app.db.createBook(book.name, self.app.userid, current_time)
            
             # 1.1 get the ID of the book we created just now
            bookresult = self.app.db.retrieveBookByCreatedTime(current_time)
            self.app.currentBookId = bookresult[0][0]
            book.localOnly = False
        
        
        chapter = self.app.currentChapter
        title = chapter.title
        content = chapter.content

        if chapter.localOnly:
            self.app.db.createChapter(title = title, 
                                      content = content, 
                                      bookid = self.app.currentBookId, 
                                      createdTime = current_time)
            
            
            # 1.1 get the ID of the book we created just now
            chapterResult = self.app.db.retrieveChapterByCreatedTime(current_time)
            self.app.currentChapterId = chapterResult[0][0]
            chapter.id = chapterResult[0][0]
            
            chapter.localOnly = False
            
            # update back the newly created id
        else:
            self.app.db.updateChapter(title, content, chapter.id)

        self.app.currentChapter.status = 'Ok'

    def export_text_file(self):
        self.app.current_filename = asksaveasfilename(
            defaultextension = ".txt",
            filetypes = [("Text Files", "*.txt"), ("All Files", "*.*")],
        )

        if not self.app.current_filename:
            return

        with open(self.app.current_filename, mode = "w", encoding = "utf-8") as output_file:
            
            writePage = self.app.getPage("WriteArea")
            
            if writePage:
                text = writePage.get_content()
                output_file.write(text)

    def new_file(self):
        current_time = datetime.now()

        newChapter = DBChapter(id = 0, 
                            title = '', 
                            content = '', 
                            bookid = self.app.currentBookId,
                            created_time = current_time,
                            localOnly = True)

        self.app.contentPage.addChapter(newChapter)
        self.app.currentChapter = newChapter
        self.app.writeArea.draw()
        self.app.refresh() 
        self.save_file()

    def delete_file(self, chapter):
        if not chapter.localOnly:
          self.app.db.deleteChapter(chapter.id)
          self.app.book.removeChapter(chapter)
        self.app.refresh()