from Device import InternetDevice


class Phone(InternetDevice):

  def __init__(self, name, model):
    super().__init__(name)
    self.model = model
    self.InstallList = []

  def print_info(self):
    print(self.model)
    super().print_info()

  def install(self, app):
    print(f'{self.name}的下载列表添加了一个软件叫{app.name}')
    self.InstallList.append(app)
