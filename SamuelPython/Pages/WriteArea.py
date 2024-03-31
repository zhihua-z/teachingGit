import tkinter as tk
from Page import Page

class WriteArea(Page):
    
    def __init__(self, app):
        super().__init__(app)
        self.content = None
        
        self.titleFont = ('Times New Roman',29,'bold')
        self.textFont = ('Helveica',16)
    
    def draw(self):
        self.clear()
        
        self.frame = tk.Frame(width=800, height=700)
        self.frame.place(x=150, y=0)
        self.register(self.frame)
    
        # 把这个Text组件画到当前frame上
        self.content = tk.Text(master=self.frame, width=130, height=700, font = self.textFont)
        self.content.place(x = 0, y = 0)
        self.register(self.content)
        
        # Default text for a new file 
        if self.app.currentChapter is not None:
            text = self.app.currentChapter.content
            self.content.delete("1.0", tk.END)
            
            self.content.insert(tk.END, text)
            
            self.content.tag_config("h1", font = self.titleFont)
            self.content.tag_config("p", font = self.textFont)
            self.content.bind('<<modified>>', self.changed)
            self.content.tag_add("h1", "1.0", "2.0")
        
    def get_content(self):
        text = self.content.get("1.0", tk.END)
        return text
    
    def changed(self):
        self.draw()
    
    def getCharacterCount(self):
        text = self.content.get("1.0", tk.END)
        count = 0
        # Loop through every index in the text 
        for i in text:
            if i != " " and i != "\n":
                count += 1
        return count
    
    def getWordCount(self):
        text = self.content.get("1.0", tk.END)
        words = text.split(" " or "," or "\n")
        return len(words)