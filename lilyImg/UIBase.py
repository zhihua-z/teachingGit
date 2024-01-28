import tkinter as tk


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
    
  def destroy(self):
    if self.label is not None:
      self.label.destroy()
      self.entry.destroy()
      self.button.destroy()
    
  


class Panel:
  def __init__(self, app, width, height):
    self.app = app
    self.width = width
    self.height = height
    
    # 储存当前面板全部的UI元素
    self.components = []
    
  def setup(self, x, y):
    pass
    
  def register(self, comp):
    self.components.append(comp)
    
  def clear(self):
    for x in self.components:
      x.destroy()
      
    self.components = []