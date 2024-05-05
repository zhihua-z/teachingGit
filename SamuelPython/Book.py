import tkinter as tk 

class Book:
    def __init__(self, bookName):
        self.name = bookName
        self.chapters = []
        
    def addChapter(self, chapter):
        if chapter.name == '':
            chapter.name = '第' + str(len(self.chapters) + 1) + '章'
        self.chapters.append(chapter)

class Chapter:
    def __init__(self, chapName = '', content = '', filePath = ''):
        self.name = chapName
        self.prevContent = content
        self.content = content
        self.filePath = filePath
        self.status = 'Ok'
        
class DBBook:
    def __init__(self, id, name, userid, created_time, localOnly = False):
        self.id = id
        self.name = name
        self.userid = userid
        self.created_time = created_time
        
        self.chapters = []
        self.localOnly = localOnly

    def addChapter(self, chapter):
        if chapter.title == '':
            chapter.title = '第' + str(len(self.chapters) + 1) + '章'
        self.chapters.append(chapter)
        
class DBChapter:
    def __init__(self, id, title, content, bookid, created_time, localOnly = False):
        self.id = id
        self.title = title
        self.prevContent = content
        self.content = content
        self.bookid = bookid
        self.creatd_time = created_time
        
        self.status = 'Ok'
        self.localOnly = localOnly