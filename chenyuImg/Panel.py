class Panel:
  def __init__(self, app, size, styles):
    self.app = app
    self.comp_list = []
    self.size = size
    self.styles = styles
    
  def setup(self):
    pass
  
  def clear(self):
    for x in self.comp_list:
      x.destroy()
    
  def register(self, comp):
    self.comp_list.append(comp)

# useless comment
