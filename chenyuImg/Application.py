import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from CYMath import Vector2
from AdjustPanel import AdjustPanel
from CropPanel import CropPanel
from EffectPanel import EffectPanel
from MenuPanel import MenuPanel

class Layer:
    def __init__(self, img = None):
        self.image = img
        self.brightness_val = 0
        
        self.result_image = None
        
    def render(self):
        self.result_image = process.adjust_brightness(self.image, self.brightness_val)
        return self.result_image



class Application:
  def __init__(self):
    self.filename = ''
    self.original_image = None
    self.current_image = None
    
    self.layer = []
    self.current_layer_index = None;
    
    self.crop_A_layer = None
    self.crop_B_layer = None
    
    self.lblImage = None
    self.on_selecting_A = False
    self.on_selecting_B = False
    
    self.control_down = False
    
    self.viewport_width = 0
    self.viewport_height = 0
    
    self.adjust_panel = AdjustPanel(self, Vector2(400, 600))
    self.effect_panel = EffectPanel(self, Vector2(400, 600))
    self.crop_panel = CropPanel(self, Vector2(400, 600))
    self.menu_panel = MenuPanel(self, Vector2(100, 600))
    
    # maintain两个list，一个是viewport里全部的组件
    # 一个是button frame里全部的组件
    self.vp_list = []
        
  def register(self, frame, tkComp):
    if frame == self.viewport:
      self.vp_list.append(tkComp)

  def setup(self):
    
    self.window = tk.Tk()

    self.menu_panel.setup()
    self.viewport = tk.Frame(width=800, height=600)
    self.viewport.pack(side=tk.LEFT)
    self.viewport_width = 800
    self.viewport_height = 600


    self.window.bind("<Button-1>", self.handle_mouse_click)
    self.window.bind('<KeyPress>',self.key_press)
    self.window.bind('<KeyRelease>',self.key_released )
    
    self.adjust_panel.setup()
    
  # if this is called, clear all the panel and draw the selected panel
  def switch(self, panel_name):
    self.adjust_panel.clear()
    self.effect_panel.clear()
    self.crop_panel.clear()
    
    if panel_name == 'adjust_panel':
      self.adjust_panel.setup()
    elif panel_name == 'effect_panel':
      self.effect_panel.setup()
    elif panel_name == 'crop_panel':
      self.crop_panel.setup()
    
      
  def key_press(self, event):
    print(event)
    
  def key_released(self, event):
    print(event)
  
  def update(self):
      self.window.mainloop()
      
  def update_render(self):
      layer = self.layer[self.current_layer_index]
      
      result_image = layer.render()
      
      if self.crop_A_layer is not None and self.crop_B_layer is not None:
          merged_crop_image = process.merge_crop(self.crop_A_layer.image, self.crop_B_layer.image)
          result_image = process.render_crop(result_image, merged_crop_image)
      elif self.crop_A_layer is not None:
          result_image = process.render_crop(result_image, self.crop_A_layer.image)
      elif self.crop_B_layer is not None:
          result_image = process.render_crop(result_image, self.crop_B_layer.image)
      
      
      self.render_image(result_image)
      
  def destroy_if_have(self, component):
      if len(self.filename) != 0 and component is not None:
          component.destroy()
  
  def render_image(self, image):
      # 清理垃圾
      self.destroy_if_have(self.lblImage)
      image1 = ImageTk.PhotoImage(image)
      self.lblImage = tk.Label(master=self.viewport, image=image1)
      self.lblImage.image = image1
      
      # 调整照片的位置让它居中
      mid_x_pos, mid_y_pos = 0, 0
      if (self.original_image.width > self.original_image.height):
        mid_y_pos = self.viewport_height / 2 - self.original_image.height / 2 - 1
      else:
        mid_x_pos = self.viewport_width / 2 - self.original_image.width / 2 - 1
        
      
      self.lblImage.place(x = mid_x_pos, y = mid_y_pos)
      self.register(self.viewport, self.lblImage)

  def update_current_layer(self, id):
      self.current_layer_index = id


  def screen_position_to_image_position(self, screen_position):
      # mouse calibration
      cx, cy = -3, -5
      
      return [screen_position[0] + cx, screen_position[1] + cy]

  def handle_mouse_click(self, event):
      # it means you just clicked crop A
      if self.on_selecting_A:
          self.on_selecting_A = False

          img_pos = self.screen_position_to_image_position((event.x, event.y))

          current_layer = self.layer[self.current_layer_index]
          self.crop_A_layer = Layer()
          self.crop_A_layer.image = process.create_crop_layer(current_layer.image, 'h', img_pos[1], 'A', True)
          self.crop_A_layer.image = process.create_crop_layer(self.crop_A_layer.image, 'v', img_pos[0], 'A', False)

          self.update_render()
      elif self.on_selecting_B:
          self.on_selecting_B = False

          img_pos = self.screen_position_to_image_position((event.x, event.y))

          current_layer = self.layer[self.current_layer_index]
          self.crop_B_layer = Layer()
          self.crop_B_layer.image = process.create_crop_layer(current_layer.image, 'h', img_pos[1], 'B', True)
          self.crop_B_layer.image = process.create_crop_layer(self.crop_B_layer.image, 'v', img_pos[0], 'B', False)

          self.update_render()


