import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2



class MenuPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y, background='#111111', highlightbackground='#111111')
    self.master.pack(side=tk.LEFT)
    self.register(self.master)
    
    t = tk.Button(master = self.master, text='Adjust', command=self.open_adjust_panel, highlightbackground='#111111')
    t.place(x=10, y=10)
    self.register(t)
    
    t = tk.Button(master = self.master, text='Effect', command=self.open_effect_panel, highlightbackground='#111111')
    t.place(x=10, y=50)
    self.register(t)
    
    t = tk.Button(master = self.master, text='Crop', command=self.open_crop_panel, highlightbackground='#111111')
    t.place(x=10, y=90)
    self.register(t)
    
  def open_adjust_panel(self):
    self.app.switch('adjust_panel')
    
    
  def open_effect_panel(self):
    self.app.switch('effect_panel')
    
    
  def open_crop_panel(self):
    self.app.switch('crop_panel')
