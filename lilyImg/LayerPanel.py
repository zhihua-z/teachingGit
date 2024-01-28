import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from Layer import Layer
    
class LayerPanel(Panel):
  def __init__(self, app, width, height):
    super().__init__(app, width, height)
    
  def setup(self, x, y):
    self.clear()
    
    super().setup(x, y)
    self.frame = tk.Frame(width=self.width, height=self.height, background='#eeeeee')
    self.frame.place(x = x, y = y)
    self.register(self.frame)
    
    temp_pos_x = 10
    for l in self.app.layer:
      t = tk.Button(master=self.frame, text=l.name)
      t.place(x = temp_pos_x, y = 10)
      self.register(t)
      
      temp_pos_x += 100
  