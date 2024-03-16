import tkinter as tk
from Page import Page

class WriteArea(Page):
    
    def __init__(self, app):
        super().__init__(app)
        self.content = None
    
    def draw(self):
        self.frame = tk.Frame(width=800, height=700)
        self.frame.place(x=150, y=0)
        self.register(self.frame)
    
        # 把这个Text组件画到当前frame上
        self.content = tk.Text(master=self.frame, width=130, height=700)
        self.content.place(x = 0, y = 0)
        self.register(self.content)
        
    def get_content(self):
        text = self.content.get("1.0", tk.END)
        return text
    
    # Google docs counts spaces as characters ], however, I have imrpoved on 
    # excluding spaces from being counted as characters to help the client with 
    # more precised character count
    def getCharacterCount(self):
        text = self.content.get("1.0", tk.END)
        count = 0
        # Loop through every index in the text 
        for i in text:
            if i != " ":
                count += 1
        return count
    
    def getWordCount(self):
        text = self.content.get("1.0", tk.END)
        # "split()" is usually used to split a string intio many substrings, spaces are used as seperators by default
        # The original string will be privided to the "split()" method and returned as substrings 
        # (",") Means the comma is set as the seperator 
        words = text.split()
        return len(words)