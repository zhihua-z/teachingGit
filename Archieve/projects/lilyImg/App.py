'''
Object Oriented Programming
- treat everything as object and simulate the real life problem using these objects

Encapsulation
Inheritance
Polymorphism
'''

from math import e
import tkinter as tk
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename
from PIL import Image
from PIL import ImageTk
import process


class Position:
  def __init__(self, x, y):
    self.x = x
    self.y = y


class ButtonGroupValInt:
  # 创建一个btnGroupValInt物体
  def __init__(self, frame, lblText, btnText, basePosition, fn):
    self.p = basePosition
    self.f = frame
    self.lt = lblText
    self.bt = btnText
    self.bp = basePosition
    self.fn = fn

    self.label = None
    self.entry = None
    self.button = None

  # 渲染这个物体
  def show(self):
    
    if self.label is not None:
      self.label.destroy()
    
    if self.entry is not None:
      self.entry.destroy()

    if self.button is not None:
      self.button.destroy()

    self.label = tk.Label(master=self.f, text=self.lt)
    self.label.place(x = self.p.x, y = self.p.y)

    self.entry = tk.Entry(master=self.f, width=5)
    self.entry.place(x = self.p.x + 90, y = self.p.y)

    self.button = tk.Button(master=self.f, text=self.bt, command=self.fn)
    self.button.place(x = self.p.x, y = self.p.y + 30)

class LilyImage:
  def __init__(self):
    self.path = ''
    self.image = None
    self.photo_image = None
    self.image_label = None
    
    self.final_result = None
    
    self.brightness = 0
    self.vibrance = 50
    
  
  def open(self, filePath):
    self.path = filePath
    self.image = Image.open(filePath)
  
  def render(self, _f, _x, _y):
    
    # apply brightness
    t_image = process.adjust_brightness(self.image, self.brightness)
    
    # apply vibrance
    t_image = process.adjust_vibrance(t_image, self.vibrance)
    
    # apply contrast
    # t_image = process.adjust_saturation(t_image, self.saturation)
    
    # apply saturation
    
    # ...
    
    self.final_result = t_image

    self.clear()

    self.photo_image = ImageTk.PhotoImage(t_image)
    self.image_label = tk.Label(master=_f, image=self.photo_image)
    self.image_label.image = self.photo_image
    self.image_label.place(x = _x, y = _y)
  
  def clear(self):
    if len(self.path) != 0 and self.image_label is not None:
      self.image_label.destroy()

class App:
  def __init__(self):
    # main app window
    self.window = None
    self.current_file = ''
    self.mainImage = LilyImage()
    self.lblImage = None
    self.o_img = None
    self.t_img = None
    
    self.layer = []
    self.setup()
  
  def setup(self):
    self.window = tk.Tk()
    
    # Frame : div 
    self.frame_main = tk.Frame(width=1000, height=800)
    self.frame_main.pack(side=tk.LEFT)

    self.frame_right = tk.Frame(width=300, height=800)
    self.frame_right.pack(side=tk.LEFT)

    self.btnOpen = tk.Button(master=self.frame_right, text='open file', command=self.open_a_file)
    self.btnOpen.place(x = 10, y = 30)

    self.btnSave = tk.Button(master=self.frame_right, text = 'save file', command=self.save_a_file)
    self.btnSave.place(x = 100, y = 30)

    self.brightness = ButtonGroupValInt(self.frame_right, 'Brightness', 'Adjust Brightness', Position(10, 70), self.adjust_brighness)
    self.brightness.show()

    self.saturation = ButtonGroupValInt(self.frame_right, 'Saturation', 'Adjust Saturation', Position(10, 130), self.adjust_saturation)
    self.saturation.show()
    
    self.vibrance = ButtonGroupValInt(self.frame_right, 'Vibrance', 'Adjust Vibrance', Position(10, 190), self.adjust_vibrance)
    self.vibrance.show()

        
  
  def run(self):
    self.window.mainloop()
  
  
  def open_a_file(self):
    self.current_file = askopenfilename()
    
    self.mainImage.open(self.current_file)
    self.mainImage.render(self.frame_main, 0, 0)

  def save_a_file(self):
    self.current_file = asksaveasfilename()
    self.t_img.save(self.current_file)


  def adjust_brighness(self):
    val = int(self.brightness.entry.get())

    self.mainImage.brightness = val
    self.mainImage.render(self.frame_main, 0, 0)
    

  def adjust_saturation(self):
    return
  
  def adjust_vibrance(self):
    val = int(self.vibrance.entry.get())
    
    self.mainImage.vibrance = val
    self.mainImage.render(self.frame_main, 0, 0)
