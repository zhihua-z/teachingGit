import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename

from UI.Panel import panel, register
from CYMath import Vector2
from Layer import Layer

from Mystring import find_last_of

from UI.CYUI import CYtoolButtun

class ToolsPanel(Panel):
  def __init__(self, app, size: Vector2, styles):
    super().__init__(app, size, styles)
  
  def setup(self, pos_x, pos_y):
    self.clear()
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y, background=self.styles.app_bar_background)
    self.master.place(x = pos_x, y = pos_y)
    self.register(self.master)

    t = CYtoolButtun(master=self.master, 
                 text='open', 
                 command=self.ask_open_file,
                 styles=self.styles,
                 position=(10, 5))
    self.register(t)

    t = CYtoolButtun(master=self.master, 
                 text='import', 
                 command=self.ask_open_file_import,
                 styles=self.styles,
                 position=(90, 5))
    self.register(t)

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
      l = Layer(self.app.original_image, layername, self.app.filename)
      
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
      l = Layer(self.app.original_image, layername, self.app.filename)
      
      # 删掉之前的layer
      self.app.layer.append(l)
      self.app.current_layer_index = len(self.app.layer) - 1

      self.app.update_render()
      self.app.layer_panel.setup(0, 600)
  

    