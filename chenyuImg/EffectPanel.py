import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2

from UI.CYUI import CYLabel, CYButton


class EffectPanel(Panel):
  def __init__(self, app, size: Vector2, styles):
    super().__init__(app, size, styles)
    
    # below is your own button panel stuffs
    pass
  
  def setup(self, pos_x, pos_y):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, 
                           height=self.size.y,
                           background=self.styles.app_background,
                           highlightbackground=self.styles.app_background)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)
    
    t = CYLabel(master=self.master, 
                 text='this is effect panel',
                 styles=self.styles,
                 position=(5, 350))
    self.register(t)
    
    # self.button_A = Button(self.adjust_panel, 'open', self.ask_open_file, (10, 10))
            
    self.lblLabel = tk.Label(master=self.master, text='Brightness')
    self.lblLabel.place(x = 10, y = 65)
    self.register(self.lblLabel)

    self.s_adjust_brightness = tk.Scale(master = self.master, from_ = -100, to = 100, tickinterval= 1, orient=tk.HORIZONTAL, command=self.on_scale_brightness_changed)
    self.s_adjust_brightness.place(x = 100, y = 50)
    self.register(self.s_adjust_brightness)
    
    t = CYButton(master=self.master, 
                 text='extract red', 
                 command=self.on_extract_red_press,
                 styles=self.styles,
                 position=(10, 140))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='extract green', 
                 command=self.on_extract_green_press,
                 styles=self.styles,
                 position=(10, 170))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='extract blue', 
                 command=self.on_extract_blue_press,
                 styles=self.styles,
                 position=(10, 200))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='adjust_shadow', 
                 command=process.adjust_shadow,
                 styles=self.styles,
                 position=(10, 230))
    self.register(t)

    t = CYButton(master=self.master, 
                 text='adjust_hightlight', 
                 command=process.adjust_hightlight,
                 styles=self.styles,
                 position=(10, 260))
    self.register(t) 

  def on_scale_brightness_changed(self, value):
      value = int(value)
      current_layer = self.layer[self.current_layer_index]
      current_layer.brightness_val = value

      self.update_render()

  def on_extract_red_press(self):
      self.app.current_image = process.extract_channel(self.app.original_image, 'r')
      self.app.render_image(self.app.current_image)
  
  def on_extract_green_press(self):
      self.current_image = process.extract_channel(self.original_image, 'g')
      self.render_image(self.current_image)
      

  def on_extract_blue_press(self):
      self.current_image = process.extract_channel(self.original_image, 'b')
      self.render_image(self.current_image)

  def on_extract_original_press(self):
      self.current_image = process.extract_channel(self.original_image, 'rgb')
      self.render_image(self.current_image)

