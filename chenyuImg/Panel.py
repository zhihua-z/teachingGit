class Panel:
  def __init__(self, app, size):
    self.app = app
    self.comp_list = []
    self.size = size
    
  def setup(self):
    pass
  
  def clear(self):
    for x in self.comp_list:
      x.destroy()
    
    self.comp_list.clear()
    
  def register(self, comp):
    self.comp_list.append(comp)

# useless comment
