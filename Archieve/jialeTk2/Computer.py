from Device import InternetDevice


class Computer(InternetDevice):

  def __init__(self, name, brand, cpu, ram):
    super().__init__(name)
    self.brand = brand
    self.cpu = cpu
    self.ram = ram

  def print_info(self):
    print(f'品牌: {self.brand}, 配置: {self.cpu}, {self.ram}')
    super().print_info()
