import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from Layer import Layer
    
class CropPanel(Panel):
  def __init__(self, app, width, height):
    super().__init__(app, width, height)
    
    
  def setup(self, x, y):
    super().setup(x, y)
    self.frame = tk.Frame(width=self.width, height=self.height)
    self.frame.place(x = x, y = y)
    self.register(self.frame)
    
    t = tk.Button(master=self.frame, text='select A')
    t.place(x = 10, y = 30)
    self.register(t)

    t = tk.Button(master=self.frame, text = 'select B')
    t.place(x = 10, y = 90)
    self.register(t)
    
  