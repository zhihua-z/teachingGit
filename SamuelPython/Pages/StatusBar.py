import tkinter as tk

from Page import Page

class StatusBar(Page):
    
    def __init__(self, app):
        super().__init__(app)
        
        self.frame = None
        
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width = 1250, height = 25)
        self.frame.place(x = 0, y = 700)
        self.register(self.frame)
    
        wordCount = str(self.app.getPage("WriteArea").getWordCount())
        chracterCount = str(self.app.getPage("WriteArea").getCharacterCount())
        
        # label to show word count
        t = tk.Label(master=self.frame, text="word count: ")
        t.place(x = 10, y = 1)
        self.register(t)
        
        t = tk.Label(master=self.frame, text=wordCount)
        t.place(x = 110, y = 1)
        self.register(t)
        
        # label to show character count
        t = tk.Label(master=self.frame, text="character count: ")
        t.place(x = 210, y = 1)
        self.register(t)
        
        t = tk.Label(master=self.frame, text=chracterCount)
        t.place(x = 310, y = 1)
        self.register(t)