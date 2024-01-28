import tkinter as tk
from UIBase import Position, ButtonGroupValInt, Panel
from tkinter.filedialog import askopenfilename, asksaveasfile, asksaveasfilename

from Layer import Layer
    
class AdjustPanel(Panel):
  def __init__(self, app, width, height):
    super().__init__(app, width, height)
    
    
  def setup(self, x, y):
    super().setup(x, y)
    self.frame = tk.Frame(width=self.width, height=self.height)
    self.frame.place(x = x, y = y)
    self.register(self.frame)
    
    t = tk.Button(master=self.frame, text='open file', command=self.open_a_file)
    t.place(x = 10, y = 30)
    self.register(t)

    t = tk.Button(master=self.frame, text = 'save file', command=self.save_a_file)
    t.place(x = 100, y = 30)
    self.register(t)

    self.brighness = ButtonGroupValInt(self.frame, 'Brightness', 'Adjust Brightness', Position(10, 70), self.adjust_brighness)
    self.brighness.show()
    self.register(self.brighness)

    self.saturation = ButtonGroupValInt(self.frame, 'Saturation', 'Adjust Saturation', Position(10, 130), self.adjust_saturation)
    self.saturation.show()
    self.register(self.saturation)
    
    self.vibrance = ButtonGroupValInt(self.frame, 'Vibrance', 'Adjust Vibrance', Position(10, 190), self.adjust_vibrance)
    self.vibrance.show()
    self.register(self.vibrance)
    
  def open_a_file(self):
    self.app.current_file = askopenfilename()
    
    if self.app.current_file == '':
      return
    
    l = Layer()
    l.open(self.app.current_file)
    l.name = 'image' + str(len(self.app.layer))
    
    self.app.layer.append(l)
    self.app.current_layer_index = 0 #len(self.app.layer) - 1
    
    self.app.update_render()
    self.app.update_layer()

  def save_a_file(self):
    self.app.current_file = asksaveasfilename()
    self.app.current_image.save(self.app.current_file)


  def adjust_brighness(self):
    val = int(self.brightness.entry.get())

    l = self.app.layer[self.app.current_layer_index]

    l.brightness = val
    self.app.update_render()
    

  def adjust_saturation(self):
    return
  
  def adjust_vibrance(self):
    val = int(self.vibrance.entry.get())
    
    l = self.app.layer[self.app.current_layer_index]

    l.vibrance = val
    self.app.update_render()
    
