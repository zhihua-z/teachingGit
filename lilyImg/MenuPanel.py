import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
    
class MenuPanel(Panel):
  def __init__(self, app, width, height):
    super().__init__(app, width, height)
    self.bg = 'white'
    self.frame = tk.Frame(width=width, height=height, background=self.bg)
    
  def setup(self, x, y):
    super().setup(x, y)
    self.frame.place(x = x, y = y)
    self.register(self.frame)
    
    t = tk.Button(master=self.frame, text='Adjust', highlightbackground=self.bg, command=self.switchAdjust)
    t.place(x = 10, y = 30)
    self.register(t)

    t = tk.Button(master=self.frame, text = 'Effect', highlightbackground=self.bg, command=self.switchEffect)
    t.place(x = 10, y = 90)
    self.register(t)
    
    t = tk.Button(master=self.frame, text = 'Crop', highlightbackground=self.bg, command=self.switchCrop)
    t.place(x = 10, y = 150)
    self.register(t)
  
  def switchAdjust(self):
    self.app.switch('adjust')
    
    
  def switchEffect(self):
    self.app.switch('effect')
    
    
  def switchCrop(self):
    self.app.switch('crop')
  