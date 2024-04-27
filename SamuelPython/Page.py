import tkinter as tk

class Page:
    
    def __init__(self, app):
        self.app = app
        
        # default tkinter components
        self.components = []
        
        # self made UI components
        self.UIcomponents = []
        
    def register(self, comp):
        self.components.append(comp)
        
    def registerUI(self, comp):
        self.UIcomponents.append(comp)
    
    def draw(self):
        pass
    
    def clear(self):
        for comp in self.components:
            comp.destroy()
        
        for UIcomp in self.UIcomponents:
            UIcomp.destroy()
        
        self.components.clear()
        self.UIcomponents.clear()