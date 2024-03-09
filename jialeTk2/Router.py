from Device import InternetDevice

class Router(InternetDevice):
  router_ip = {}

  def __init__(self, name, dns, ip, ip_list):
    super().__init__(name)
    self.dns = dns
    self.ip = ip

    # 缓存 路由器表
    self.cache_router = {}
    self.used_cache = {}

    # 已连接数量
    self.connect_count = 0

    # 全部可用ip列表
    self.ip_list = ip_list

    # ip占用情况列表
    self.ip_used = []

    # ip分配字典
    self.ip_dict = {}

    for i in range(len(ip_list)):
      self.ip_used.append(False)
      self.ip_dict[ip_list[i]] = None

    # 把当前路由器注册到一个字典中，小作弊的方式，现实世界中路由器都是物理连接的，所以它们天生就知道自己连着谁
    Router.router_ip[self.ip] = self

  def __str__(self):
    return self.name

  def add_cache(self, ip_rule, router_ip):
    self.cache_router[ip_rule] = router_ip

  def print_info(self):
    print(self.name, self.ip)
    print(
        f'总ip数量{len(self.ip_list)}, 可用ip数量{len(self.ip_list) - self.connect_count}'
    )

    for x in self.ip_dict:
      print(x, self.ip_dict[x])

    print('缓存规则')
    for x in self.cache_router:
      print(x, self.cache_router[x])

    print('')

  # 成功连接，返回True
  # 失败返回False
  def connect(self, device):
    # 当可用ip不足的时候，拒绝连接
    if self.connect_count == len(self.ip_list):
      return None, None

    self.connect_count += 1
    return self.dhcp_get_ip(device), self

  # DHCP在现实环境不是由路由器分配的，是由你的网络供应商提供的
  def dhcp_get_ip(self, device):
    # 找到第一个没有被分配的ip
    # 并且把这个ip标记为被占用
    # 然后记下这个ip的设备
    # 然后返回这个ip

    total_ip_amount = len(self.ip_list)

    for i in range(total_ip_amount):
      if self.ip_used[i] == False:

        thisip = self.ip_list[i]
        self.ip_used[i] = True
        self.ip_dict[thisip] = device
        return thisip

  def send(self, packet):
    # 1. 检查ttl，如果ttl没了，直接返回，啥也不做
    if packet.ttl == 0:
      print(f'{packet}的ttl为0，丢包')
      return

    # 2. 传出去
    #   2.1 如果目标地址是我直接连着的设备，发给他
    if packet.target_ip in self.ip_dict:
      device = self.ip_dict[packet.target_ip]
      if device is not None:
        packet.ttl -= 1
        device.receive(packet)
        return
      else:
        # 地址我认识，但是该设备没有联网
        return

    #   2.2 如果目标地址我不认识，但是知道大概的方向，发给那个方向
    # 如果我走到了这个位置，意味着这个ip地址我没有直连
    # 如果知道大概的方向，发给那个方向
    # 如果我能在缓存中找到这个这个ip对应的地址，我就往那个路由器发送
    # 如果缓存中找不到那个地址，我就随便找一个连接着的路由器发过去
    self.add_cache(packet.source_ip, packet.before_ip)

    packet.before_ip = self.ip

    if packet.target_ip in self.cache_router:
      # 知道是这个方向
      #        获取到那个路由器ip对应的路由器物体
      #                         获取到缓存中这个ip应该发到的路由器的ip
      router = Router.router_ip[self.cache_router[packet.target_ip]]
      packet.ttl -= 1
      router.send(packet)
      pass
    else:
      # 挑选一个随机连接着的路由器发过去
      for x in self.cache_router:
        # 如果这个缓存的ip是这个包的来源，不发
        if x == packet.before_ip:
          continue

        # # 如果x和packet的目标ip相似，我们就发到x的那个缓存上
        # # 192.168.0.2 对应着199.172.1.10
        # # 192.168.0.1 虽然不在缓存里，但是它和192.168.0.2非常相似，那么你的路由器应该试着使用192.168.0.2的缓存
        # '''     https://www.cnblogs.com/573734817pc/p/10900379.html
        # import difflib

        # #判断相似度的方法，用到了difflib库
        # def get_equal_rate_1(str1, str2):
        #    return difflib.SequenceMatcher(None, str1, str2).quick_ratio()
        # '''
        # if difflib.SequenceMatcher(None, x, packet.target_ip).quick_ratio() > 0.8:
        #   router = Router.router_ip[self.cache_router[x]]
        #   packet.ttl -= 1
        #   router.send(packet)

        if x == 'x.x.x.x':
          router = Router.router_ip[self.cache_router[x]]
          packet.ttl -= 1
          router.send(packet)

      pass
    return

  def is_ip(self, target):
    # 如果target里有//，那就是域名，否则就是ip
    # 以上是非常天真的算法，但是足够了
    if '//' in target:
      return False
    else:
      return True

  def get_ip(self, target):
    # 如果target已经是一个ip，直接返回这个ip
    # 如果target是一个域名，那就和dns服务器查询这个域名的ip，再返回ip
    if self.is_ip(target):
      return target
    else:
      return self.dns.find(target)
