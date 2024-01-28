import tkinter as tk

from Layer import Layer
from AdjustPanel import AdjustPanel
from EffectPanel import EffectPanel
from CropPanel import CropPanel

from LayerPanel import LayerPanel

from MenuPanel import MenuPanel
from Canvas import Canvas
    
class App:
  def __init__(self):
    # main app window
    self.window = None
    self.current_file = ''
    self.lblImage = None
    self.o_img = None
    self.t_img = None
    
    # 保留一个叫canvas的物品
    self.current_image = None
    
    # 保留一个列表的layers，每一个layer都会保留一张图片，最后整个图片就是由全部的layer拼接在一起
    self.layer = []
    self.current_layer_index = -1
    
    self.current_panel = ''
    
    self.setup()
  
  def setup(self):
    self.window = tk.Tk()
    self.window.geometry('1400x900')
    
    # Frame : div 
    self.canvas = Canvas(self, 1000, 800)
    self.canvas.setup(100, 0)
    
    self.adjust_panel = AdjustPanel(self, 300, 800)
    self.adjust_panel.setup(1100, 0)
    
    self.effect_panel = EffectPanel(self, 300, 800)
    #self.effect_panel.setup(1100, 0)
    
    self.crop_panel = CropPanel(self, 300, 800)
    #self.crop_panel.setup(1100, 0)
    
    self.menu_panel = MenuPanel(self, 100, 800)
    self.menu_panel.setup(0, 0)
    
    self.layer_panel = LayerPanel(self, 1400, 100)
    self.layer_panel.setup(0, 800)
        
  
  def run(self):
    self.window.mainloop()
    
  # function delegate
  def update_render(self):
    self.canvas.update_render()
    
  def update_layer(self):
    self.layer_panel.setup(0, 800)

  def switch(self, target):
    
    # if you are at adjust panel and you clicked adjust panel, do nothing
    if self.current_panel == target:
      return
    
    if self.current_panel == 'adjust':
      self.adjust_panel.clear()
    elif self.current_panel == 'effect':
      self.effect_panel.clear()
    elif self.current_panel == 'crop':
      self.crop_panel.clear()
      
    if target == 'adjust':
      self.adjust_panel.setup(1100, 0)
      self.current_panel = 'adjust'
    elif target == 'effect':
      self.effect_panel.setup(1100, 0)
      self.current_panel = 'effect'
    elif target == 'crop':
      self.crop_panel.setup(1100, 0)
      self.current_panel = 'crop'
      
    