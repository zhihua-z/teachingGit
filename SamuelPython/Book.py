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
        self.content = content
        self.filePath = filePath