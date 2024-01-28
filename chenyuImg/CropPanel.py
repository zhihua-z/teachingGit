import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2



class CropPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y)
    self.master.pack(side=tk.LEFT)
    self.register(self.master)
    
    t = tk.Label(master=self.master, text='this is crop panel')
    t.place(x = 0, y = 350)
    self.register(t)
    
    self.btn_crop_A = tk.Button(master=self.master, text = 'Crop A', command=self.on_crop_A_pressed)
    self.btn_crop_A.place(x = 10, y = 230)
    self.btn_crop_B = tk.Button(master=self.master, text = 'Crop B', command=self.on_crop_B_pressed)
    self.btn_crop_B.place(x = 70, y = 230)
    self.register(self.btn_crop_A)
    self.register(self.btn_crop_B)


  def on_crop_A_pressed(self):
      self.on_selecting_A = True
      self.on_selecting_B = False

  def on_crop_B_pressed(self):
      self.on_selecting_A = False
      self.on_selecting_B = True

