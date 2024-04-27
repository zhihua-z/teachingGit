import tkinter as tk
from PIL import Image, ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2
from Layer import Layer

from Mystring import find_last_of

from CYUI import CYLabel, CYButton
import styles

class AdjustPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self, pos_x, pos_y):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y, background=styles.app_background)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)

    t = CYLabel(master=self.master, 
                 text='this is adjust panel',
                 position=(5, 350))
    self.register(t)
    
    # self.button_A = Button(self.adjust_panel, 'open', self.ask_open_file, (10, 10))
    self.lblLabel = tk.Label(master=self.master, text='Brightness')
    self.lblLabel.place(x = 10, y = 50)
    self.register(self.lblLabel)
    

    self.s_adjust_brightness = tk.Entry(master = self.master)
    self.s_adjust_brightness.place(x = 100, y = 50)
    self.register(self.s_adjust_brightness)
    
    t = tk.Button(master=self.master, text='Adjust brightness', command=self.on_brightness_changed)
    t.place(x = 150, y = 50)
    self.register(t)

    t = CYButton(master=self.master, 
                 text='extract red', 
                 command=self.on_extract_red_press,
                 position=(90, 140))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='extract green', 
                 command=self.on_extract_green_press,
                 position=(90, 170))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='extract blue', 
                 command=self.on_extract_blue_press,
                 position=(90, 200))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='back_original', 
                 command=self.on_extract_original_press,
                 position=(90, 230))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='adjust_shadow', 
                 command=process.adjust_shadow,
                 position=(90, 230))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='adjust_hightlight', 
                 command=process.adjust_hightlight,
                 position=(90, 260))
    self.register(t) 

  def on_brightness_changed(self):
      if self.app.layer is None or len(self.app.layer) == 0:
          return
      
      value = int(self.s_adjust_brightness.get())
      current_layer = self.app.layer[self.app.current_layer_index]
      current_layer.brightness_val = value

      self.app.update_render()

  def on_extract_red_press(self):
      if self.app.layer is None or len(self.app.layer) == 0:
          return
      
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.red:
          layer.channel = layer.channel - Layer.red
        else:
          layer.channel = layer.channel + Layer.red
          
        # layer.channel |= Layer.red
      
      self.app.update_render()
  
  def on_extract_green_press(self):
      if self.app.layer is None or len(self.app.layer) == 0:
          return
      
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.green:
          layer.channel = layer.channel - Layer.green
        else:
          layer.channel = layer.channel + Layer.green
      
      self.app.update_render()
      

  def on_extract_blue_press(self):
      if self.app.layer is None or len(self.app.layer) == 0:
          return
      
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.blue:
          layer.channel = layer.channel - Layer.blue
        else:
          layer.channel = layer.channel + Layer.blue
      
      self.app.update_render()

  def on_extract_original_press(self):
      if self.app.layer is None or len(self.app.layer) == 0:
          return
      
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        layer.channel = 15
      
      self.app.update_render()
