import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2
from Layer import Layer

from Mystring import find_last_of

class AdjustPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self, pos_x, pos_y):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)
    
    self.register(self.master)
    t = tk.Label(master=self.master, text='this is button panel')
    t.place(x = 0, y = 350)
    self.register(t)
    
    self.btn_open = tk.Button(master = self.master, text='open', command=self.ask_open_file)
    self.btn_open.place(x=10, y=10)
    self.register(self.btn_open)
    
    
    t = tk.Button(master = self.master, text='import', command=self.ask_open_file_import)
    t.place(x=90, y=10)
    self.register(t)
    
    # self.button_A = Button(self.adjust_panel, 'open', self.ask_open_file, (10, 10))
            
    self.lblLabel = tk.Label(master=self.master, text='Brightness')
    self.lblLabel.place(x = 10, y = 65)
    self.register(self.lblLabel)

    self.s_adjust_brightness = tk.Scale(master = self.master, from_ = -100, to = 100, tickinterval= 1, orient=tk.HORIZONTAL, command=self.on_scale_brightness_changed)
    self.s_adjust_brightness.place(x = 100, y = 50)
    self.register(self.s_adjust_brightness)

    self.btn_extract_red = tk.Button(master=self.master, text='extract red', command=self.on_extract_red_press)
    self.btn_extract_red.place(x = 10, y = 110)
    self.register(self.btn_extract_red)

    self.btn_extract_green = tk.Button(master=self.master, text='extract green', command=self.on_extract_green_press)
    self.btn_extract_green.place(x = 10, y = 140)
    self.register(self.btn_extract_green)

    self.btn_extract_blue = tk.Button(master=self.master, text='extract blue', command=self.on_extract_blue_press)
    self.btn_extract_blue.place(x = 10, y = 170)
    self.register(self.btn_extract_blue)

    self.btn_extract_original = tk.Button(master=self.master, text='original', command=self.on_extract_original_press)
    self.btn_extract_original.place(x = 10, y = 200)
    self.register(self.btn_extract_original)

    self.btn_adjust_shadow = tk.Button(master=self.master,text= 'adjust_shadow',command= process.adjust_shadow)
    self.btn_adjust_shadow.place(x = 10, y = 260)
    self.register(self.btn_adjust_shadow)

    self.btn_adjust_hightlight = tk.Button(master=self.master,text= 'adjust_hightlight',command= process.adjust_hightlight)
    self.btn_adjust_hightlight.place(x = 90, y = 260)
    self.register(self.btn_adjust_hightlight)
  
  
  def ask_open_file(self):
      self.app.filename = askopenfilename(filetypes=[("Image files","*.bmp *.png *.jpg *.webp")])

      # imagename = './clock.jpg'
      if len(self.app.filename) == 0:
          return
      
      self.app.original_image = Image.open(self.app.filename)
      # self.app.original_image.save('output.jpg')
      
      # 如果我的照片横向纵向都比viewport小，我就需要调大这张照片
      # 如果我的照片横向或者纵向比viewport大，我就需要根据一个比例来调整
      # 调整的目标是：最大的那条边满足于屏幕的大小 800 x 600
      
      # 如果我的照片横向是1000，纵向是1500，我的屏幕尺寸是800x600，那我应该怎样调整？
      
      # 找比较长的边
      if (self.app.original_image.width > self.app.original_image.height):
        # 调整横边
        ratio = self.app.viewport_width / self.app.original_image.width
      else:
        # 调整竖边
        ratio = self.app.viewport_height / self.app.original_image.height
      new_sz = (round(self.app.original_image.width * ratio), round(self.app.original_image.height * ratio))
      self.app.original_image = self.app.original_image.resize(new_sz, resample = Image.Resampling.BICUBIC)
      self.app.current_image = self.app.original_image
      
      # remove the full path from file name
      last_pos = find_last_of(self.app.filename, '/')
      layername = self.app.filename[last_pos + 1:]
      
      # 管理layer
      l = Layer(self.app.original_image, layername)
      
      # 删掉之前的layer
      self.app.layer = self.app.layer[:-1]
      self.app.layer.append(l)
      self.app.current_layer_index = 0

      self.app.render_image(self.app.original_image)
      self.app.layer_panel.setup(0, 600)
      
  def ask_open_file_import(self):
      self.app.filename = askopenfilename(filetypes=[("Image files","*.bmp *.png *.jpg *.webp")])

      # imagename = './clock.jpg'
      if len(self.app.filename) == 0:
          return
      
      self.app.original_image = Image.open(self.app.filename)
      
      # remove the full path from file name
      last_pos = find_last_of(self.app.filename, '/')
      layername = self.app.filename[last_pos + 1:]
      
      # 管理layer
      l = Layer(self.app.original_image, layername)
      
      # 删掉之前的layer
      self.app.layer.append(l)
      self.app.current_layer_index = len(self.app.layer) - 1

      self.app.update_render()
      self.app.layer_panel.setup(0, 600)

  def on_scale_brightness_changed(self, value):
      value = int(value)
      current_layer = self.layer[self.current_layer_index]
      current_layer.brightness_val = value

      self.update_render()

  def on_extract_red_press(self):
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.red:
          layer.channel = layer.channel - Layer.red
        else:
          layer.channel = layer.channel + Layer.red
          
        # layer.channel |= Layer.red
      
      self.app.update_render()
  
  def on_extract_green_press(self):
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.green:
          layer.channel = layer.channel - Layer.green
        else:
          layer.channel = layer.channel + Layer.green
      
      self.app.update_render()
      

  def on_extract_blue_press(self):
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        if layer.channel & Layer.blue:
          layer.channel = layer.channel - Layer.blue
        else:
          layer.channel = layer.channel + Layer.blue
      
      self.app.update_render()

  def on_extract_original_press(self):
      layer = self.app.layer[self.app.current_layer_index]
      
      if layer:
        layer.channel = 15
      
      self.app.update_render()
