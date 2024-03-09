from Packet import Packet


class Device:

  def __init__(self, name):
    self.name = name

  # 打印这个设备名字
  def __str__(self):
    return self.name

  # 打印具体信息
  def print_info(self):
    print(f'{self.name}')


class InternetDevice(Device):

  def __init__(self, name):
    super().__init__(name)
    self.connected = False
    self.ip = None
    self.router = None

  # 打印这个设备名字
  def __str__(self):
    return self.name

  # 打印具体信息
  def print_info(self):
    print(f'{self.name}')
    if self.connected:
      print(f'有网络连接，路由器为: {self.router.name}, ip地址为{self.ip}')
    else:
      print('无网络连接')

  def connect(self, luyouqi):
    # 元组赋值
    self.ip, self.router = luyouqi.connect(self)

    if self.ip is not None:
      self.connected = True

  def send(self, message, target_ip):
    target_ip = self.router.get_ip(target_ip)

    packet = Packet(message, self.ip, target_ip)
    self.router.send(packet)

  def receive(self, packet):
    print(f'{self.name}收到了一个数据包，内容为：|{packet}|')


class DNS_server(Device):

  def __init__(self):
    super().__init__('DNS 服务器')
    # 192.168.x.x段ip其实应该是内网IP，只是目前我们还不管ip的分段，我们就把ip当做一个普通地址使用
    self.dns_dict = {
        '192.168.0.1': 'http://我的手机.com',
        '192.168.0.2': 'http://我的电脑.com',
        '192.168.0.3': 'http://我的电脑2.com',
        '10.0.0.1': 'http://小花的手机.com',
        '192.168.0.4': 'http://我的d30.com',
        'http://我的手机.com': '192.168.0.1',
        'http://我的电脑.com': '192.168.0.2',
        'http://我的电脑2.com': '192.168.0.3',
        'http://小花的手机.com': '10.0.0.1',
        'http://我的d30.com': '192.168.0.4'
    }

  def find(self, input):
    if input in self.dns_dict:
      return self.dns_dict[input]
    else:
      return None

  def buy_domain(self, yuming, ip):
    self.dns_dict[yuming] = ip
    self.dns_dict[ip] = yuming
