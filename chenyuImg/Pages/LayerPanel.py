import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2



class LayerPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self, pos_x, pos_y):
    self.clear()
    super().setup()
    
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)
    
    curr_position = (10, 10)
    # for each layer the application have, make a new layer button
    for layer in self.app.layer:
      t = tk.Button(master = self.master, text=layer.name, command=lambda l=layer:self.switchlayer(l))
      t.place(x = curr_position[0], y = curr_position[1])
      self.register(t)
      
      curr_position = (curr_position[0] + 100, curr_position[1])
    
  def switchlayer(self, layer):
    pos_x = self.app.click_pos[0]
    pos_x = pos_x - 10
    
    
    layer_index = 0
    
    # 找这个layer index
    for l in self.app.layer:
      if l.name == layer.name:
        layer_index = self.app.layer.index(l)
    
    self.app.current_layer_index = layer_index
    self.app.update_render()
    
    # to switch between image without the layer merge system, you don't need to use update_render
    # use self.app.render_image() instead
