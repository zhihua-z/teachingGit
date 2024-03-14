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
    
    def getCharacterCount(self):
        text = self.content.get("1.0", tk.END)
        return len(text)