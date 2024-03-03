import tkinter as tk


class ContentPage:
    
    def __init__(self, app):
        self.app = app
    
    def draw(self):
        self.frame = tk.Frame(width=150, height=700, background='#dddddd')
        self.frame.place(x=0, y=0)