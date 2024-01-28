import tkinter as tk
from PIL import Image
from PIL import ImageTk
from tkinter.filedialog import askopenfilename
import process

from Panel import Panel
from CYMath import Vector2

class AdjustPanel(Panel):
  def __init__(self, app, size: Vector2):
    super().__init__(app, size)
  
  def setup(self):
    super().setup()
    
    self.master = tk.Frame(width=self.size.x, height=self.size.y)
    self.master.pack(side=tk.LEFT)
    self.register(self.master)
    
    self.register(self.master)
    t = tk.Label(master=self.master, text='this is button panel')
    t.place(x = 0, y = 350)
    self.register(t)
    
    self.btn_open = tk.Button(master = self.master, text='open', command=self.ask_open_file)
    self.btn_open.place(x=10, y=10)
    self.register(self.btn_open)
    
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
      
      # 管理layer
      l = Layer(self.app.original_image)
      
      # 删掉之前的layer
      self.app.layer = self.app.layer[:-1]
      self.app.layer.append(l)
      self.app.current_layer_index = 0

      self.app.render_image(self.app.original_image)

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
