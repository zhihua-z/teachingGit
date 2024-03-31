
class Packet:

  def __init__(self, msg, source_ip, target_ip):
    self.msg = msg
    self.source_ip = source_ip
    self.target_ip = target_ip
    self.before_ip = None
    self.ttl = 10

  def __str__(self):
    return f'数据包｜内容：{self.msg}, 来自{self.source_ip}, 发给{self.target_ip}'
