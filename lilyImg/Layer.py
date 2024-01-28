from PIL import Image
import process

class Layer:
  def __init__(self):
    self.path = ''
    self.image = None
    self.photo_image = None
    self.image_label = None
    
    self.name = self.path
    
    self.final_result = None
    
    self.brightness = 0
    self.vibrance = 50
    
  
  def open(self, filePath):
    self.path = filePath
    self.image = Image.open(filePath)
  
  def render(self):
    
    # apply brightness
    t_image = process.adjust_brightness(self.image, self.brightness)
    
    # apply vibrance
    t_image = process.adjust_vibrance(t_image, self.vibrance)
    
    # apply contrast
    # t_image = process.adjust_saturation(t_image, self.saturation)
    
    # apply saturation
    
    # ...
    
    self.final_result = t_image
  
  def clear(self):
    if len(self.path) != 0 and self.image_label is not None:
      self.image_label.destroy()
