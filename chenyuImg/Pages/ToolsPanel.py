import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2



class ToolsPanel(Panel):
  def __init__(self, app, size: Vector2, styles):
    super().__init__(app, size, styles)
  
  def setup(self, pos_x, pos_y):
    self.clear()
    super().setup()
    
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y, background=self.styles.app_bar_background)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)
    
    