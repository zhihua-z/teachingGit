import tkinter as tk

from Page import Page

class ContentPage(Page):
    
    def __init__(self, app):
        super().__init__(app)
        
        self.frame = None
    
    def draw(self):
        self.frame = tk.Frame(width=150, height=700, background='#dddddd')
        self.frame.place(x=0, y=0)
        self.register(self.frame)