import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2

from CYUI import CYImageButton
import styles

class MenuPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self, pos_x, pos_y):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, 
                           height=self.size.y, 
                           background=styles.app_background, 
                           highlightbackground=styles.app_background)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)
    
    t = CYImageButton(master = self.master,
                      image_path = 'images/btn/adjust_panel.jpg', 
                      command = self.open_adjust_panel,
                      position = (25, 10),
                      size = (40, 40),
                      label='Adjust')
    self.register(t)
    
    t = CYImageButton(master = self.master,
                      image_path = 'images/btn/effect_panel.png', 
                      command = self.open_effect_panel,
                      position = (25, 90),
                      size = (40, 40),
                      label='Effect')
    self.register(t)
    
    t = CYImageButton(master = self.master,
                      image_path = 'images/btn/crop_panel.png', 
                      command = self.open_crop_panel,
                      position = (25, 170),
                      size = (40, 40),
                      label='Crop')
    self.register(t)
    
    
  def open_adjust_panel(self):
    self.app.switch('adjust_panel')
    
    
  def open_effect_panel(self):
    self.app.switch('effect_panel')
    
    
  def open_crop_panel(self):
    self.app.switch('crop_panel')
