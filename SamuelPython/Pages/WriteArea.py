import tkinter as tk

class WriteArea:
    
    def __init__(self, app):
        self.app = app
        self.content = None
    
    def draw(self):
        self.frame = tk.Frame(width=800, height=700)
        self.frame.place(x=150, y=0)
    
        # 把这个Text组件画到当前frame上
        self.content = tk.Text(master=self.frame, width=130, height=700)
        self.content.place(x = 0, y = 0)
    