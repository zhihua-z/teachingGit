import tkinter as tk

class Page:
    
    def __init__(self, app):
        self.app = app
        
        self.components = []
        
    def register(self, comp):
        self.components.append(comp)
    
    def draw(self):
        pass
    
    def clear(self):
        for comp in self.components:
            comp.destroy()
        
        self.components.clear()